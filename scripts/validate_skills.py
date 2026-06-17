#!/usr/bin/env python3
"""Validate the QJ agent skill pack."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
SKILLS_DIR = ROOT / "skills"
EXPECTED_SKILLS = {
    "qj-equity-deep-dive",
    "qj-earnings-preview",
    "qj-earnings-recap",
    "qj-valuation-workbench",
    "qj-thesis-tracker",
    "qj-portfolio-monitor",
    "qj-congress-gov-signals",
    "qj-institutional-flow",
    "qj-macro-regime-brief",
    "qj-catalyst-calendar",
    "qj-idea-generation",
    "qj-risk-bias-review",
    "qj-portfolio-rebalance-planner",
    "qj-supply-chain-theme-research",
}
SHARED_REQUIRED = {
    "shared/references/qj-mcp-tool-map.md",
    "shared/references/evidence-standard.md",
    "shared/references/output-contract.md",
    "shared/references/compliance-boundaries.md",
    "shared/templates/tools-used.md",
    "shared/templates/thesis-tracker.md",
    "shared/templates/catalyst-calendar.md",
}
TOOL_RE = re.compile(r"`((?:data|api)\.[a-zA-Z0-9_.]+)`")


def load_tool_names(path: Path) -> set[str]:
    payload = json.loads(path.read_text())
    return {tool["name"] for tool in payload.get("tools", []) if isinstance(tool, dict) and tool.get("name")}


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("frontmatter is not closed")
    frontmatter = text[4:end]
    fields: dict[str, str] = {}
    for line in frontmatter.splitlines():
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        if not sep:
            raise ValueError(f"invalid frontmatter line: {line}")
        fields[key.strip()] = value.strip()
    return fields


def main() -> int:
    errors: list[str] = []
    actual_skills = {p.name for p in SKILLS_DIR.iterdir() if p.is_dir()}
    missing = EXPECTED_SKILLS - actual_skills
    extra = actual_skills - EXPECTED_SKILLS
    if missing:
        errors.append(f"missing skills: {sorted(missing)}")
    if extra:
        errors.append(f"unexpected skills: {sorted(extra)}")

    for rel in SHARED_REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"missing shared file: {rel}")

    data_manifest = WORKSPACE / "_repo_qj_data_mcp/data/mcp/qj-data.tools.json"
    api_manifest = WORKSPACE / "_repo_qj_api_mcp/data/mcp/domains.tools.json"
    known_tools = load_tool_names(data_manifest) | load_tool_names(api_manifest)

    for skill in sorted(EXPECTED_SKILLS):
        path = SKILLS_DIR / skill / "SKILL.md"
        if not path.is_file():
            errors.append(f"{skill}: missing SKILL.md")
            continue
        text = path.read_text()
        try:
            frontmatter = parse_frontmatter(text)
        except ValueError as exc:
            errors.append(f"{skill}: {exc}")
            continue
        if frontmatter.get("name") != skill:
            errors.append(f"{skill}: frontmatter name mismatch")
        if not frontmatter.get("description") or "TODO" in frontmatter.get("description", ""):
            errors.append(f"{skill}: missing useful description")
        if "TODO" in text or "placeholder" in text.lower() or "Structuring This Skill" in text:
            errors.append(f"{skill}: template placeholder remains")
        for tool in TOOL_RE.findall(text):
            if tool.endswith(".*"):
                continue
            if tool not in known_tools:
                errors.append(f"{skill}: unknown MCP tool `{tool}`")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"OK: validated {len(EXPECTED_SKILLS)} skills and {len(SHARED_REQUIRED)} shared files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
