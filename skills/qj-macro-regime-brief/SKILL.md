---
name: qj-macro-regime-brief
description: QJ MCP-backed macro and market regime brief workflow. Use when the user asks for rates, macro calendar, benchmark performance, commodities, market regime, cross-asset context, or macro risks for equities or portfolios.
---

# QJ Macro Regime Brief

Summarize macro context from QJ benchmark, calendar, treasury, and commodity tools.

## Workflow

1. Pull macro calendar with `data.events.macro_calendar`.
2. Pull rates with `data.benchmarks.treasury_rates`.
3. Pull benchmark context with `data.benchmarks.indices`, `data.benchmarks.quotes`, and `data.benchmarks.compare`.
4. Pull commodity context with `data.commodities.latest`, `data.commodities.prices`, and `data.commodities.inventories` when relevant.
5. For portfolio impact, add `data.portfolio.dashboard`, `data.risk.factor_exposure`, or `data.intelligence.pm_brief`.

## Required Output

- Regime snapshot: rates, benchmarks, commodities, macro calendar.
- Equity/portfolio implications.
- Watch items and upcoming macro catalysts.
- Data coverage and stale series warnings.

## Guardrails

- Do not overstate macro causality.
- Distinguish observed moves from regime interpretation.
