# QJ Agent Skills

Portable QuantJourney agent skills for MCP-backed investment research.

This repository is the research/playbook layer above:

- `qj_data_mcp`: curated QJ intelligence tools, exposed as `data.*`
- `qj_api_mcp`: raw/domain API tools, exposed as `api.*`

The skills do not fetch data directly. They instruct an agent how to orchestrate QJ MCP tools, preserve evidence, and produce research outputs with clear boundaries.

## Principles

- Prefer `data.*` tools first.
- Use `api.domains.call` only when curated `data.*` coverage is missing.
- Never scrape websites, call provider APIs directly, or install market-data packages from a skill.
- Separate `Facts`, `Interpretation`, and `Open Questions`.
- Include `Coverage` and `Tools Used` in every substantial output.
- Treat all outputs as research support, not trading instructions.

## Skill Catalog

See `SKILLS.md` for the full catalog and intended use cases.

## Layout

```text
skills/
  qj-equity-deep-dive/
  qj-earnings-preview/
  qj-earnings-recap/
  qj-valuation-workbench/
  qj-thesis-tracker/
  qj-portfolio-monitor/
  qj-congress-gov-signals/
  qj-institutional-flow/
  qj-macro-regime-brief/
  qj-catalyst-calendar/
  qj-idea-generation/
  qj-risk-bias-review/
  qj-portfolio-rebalance-planner/
  qj-supply-chain-theme-research/
shared/
  references/
  templates/
```

## Validation

Validate individual skills with:

```bash
python3 /Users/jakub/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/qj-equity-deep-dive
```

Run the same command for each folder under `skills/`.
