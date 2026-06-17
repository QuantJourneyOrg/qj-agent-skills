# Evidence Standard

Every substantial output must make data provenance visible.

## Required Sections

- `Facts`: direct observations from QJ MCP outputs. Include tool name and as-of timestamp when available.
- `Interpretation`: agent reasoning derived from facts. Do not mix unsupported claims into facts.
- `Open Questions`: missing data, stale coverage, conflicting evidence, or user inputs needed.
- `Coverage`: list data surfaces used and gaps found.
- `Tools Used`: tool names, purpose, and key parameters.

## Rules

- Prefer QJ curated `data.*` tools over raw API tools.
- Do not invent missing financial values, estimates, dates, ratings, holdings, or risk numbers.
- If two tools conflict, show the conflict and avoid forcing a single conclusion.
- If a tool returns warnings, missing data, stale timestamps, or low coverage, surface that explicitly.
- Label user-provided assumptions separately from QJ-sourced facts.

## Citation Pattern

Use compact tool citations:

```text
[tool: data.metrics.snapshot, ticker=MSFT, as_of=2026-06-17]
```

If a tool returns provider metadata, add it:

```text
[tool: data.fundamentals.latest, provider=fmp, period=FY2025]
```
