---
name: qj-portfolio-monitor
description: QJ MCP-backed portfolio monitoring workflow. Use when the user asks for a portfolio review, PM brief, holdings monitor, risk/event dashboard, exposure summary, current positions, PnL context, or watchlist monitoring.
---

# QJ Portfolio Monitor

Review a portfolio with QJ data, risk, event, and holdings context.

## Workflow

1. Confirm the portfolio node, account, or watchlist scope.
2. Pull `data.intelligence.pm_brief` when available.
3. Pull portfolio state with `data.portfolio.dashboard`, `data.portfolio.holdings`, `data.portfolio.positions`, `data.portfolio.nav`, `data.portfolio.pnl`, and `data.portfolio.attribution` as needed.
4. Pull event exposure with `data.events.exposure_summary` and `data.events.risk_summary`.
5. Pull risk context with `data.risk.info`, `data.risk.factor_exposure`, `data.risk.scenario_list`, and `data.risk.scenario_run` when authorized.
6. For key holdings, use `data.ticker.deep_dive` and `data.metrics.snapshot`.

## Required Output

- Portfolio state and major exposures.
- Top risks and upcoming events.
- Position-level watch items.
- Data gaps and permission gaps.
- Follow-up questions for the PM.

## Guardrails

- Do not propose trades unless the user asks for planning; even then, keep it as a checklist.
- Respect tenancy, auth, and read-only boundaries.
