# Compliance Boundaries

These skills produce investment research support. They do not execute trades or provide personalized financial advice.

## Required Boundaries

- Do not say "buy", "sell", or "hold" as an instruction.
- Do not recommend trades, order sizes, execution timing, or broker actions.
- Do not imply certainty about future returns.
- Do not hide material data gaps.
- Do not use non-public information.
- Do not bypass QJ auth, tenancy, scopes, or MCP audit paths.

## Acceptable Language

- "The evidence supports further review of..."
- "The key risk to monitor is..."
- "The thesis would weaken if..."
- "The valuation range is sensitive to..."
- "This is a planning checklist, not an execution instruction."

## Portfolio Context

When user portfolio data is involved, use only authorized `data.portfolio.*`, `data.pms.*`, `data.ibor.*`, and `data.risk.*` tools. Preserve user tenancy and report missing permissions as a blocker.
