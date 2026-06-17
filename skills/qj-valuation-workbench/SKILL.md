---
name: qj-valuation-workbench
description: QJ MCP-backed valuation workflow for DCF, comps, scenario tables, return sensitivity, and valuation range discussion. Use when the user asks for valuation, DCF, comps, upside/downside scenarios, margin of safety, or multiple sensitivity.
---

# QJ Valuation Workbench

Build valuation analysis from QJ-sourced facts and explicit user assumptions.

## Workflow

1. Pull company baseline with `data.ticker.deep_dive`, `data.profile.get`, and `data.prices.latest`.
2. Pull financial history with `data.fundamentals.statements`, `data.fundamentals.latest`, and `data.metrics.history`.
3. Pull current metrics with `data.metrics.snapshot` and trend context with `data.metrics.trends`.
4. Pull forward context with `data.estimates.consensus`, `data.estimates.revisions`, and `data.estimates.dispersion`.
5. For comps, use `data.metrics.screen` or user-provided peers, then call `data.metrics.snapshot` per peer or use `data.fundamentals.batch` for safe grouped fundamentals.
6. Use user-provided assumptions for WACC, growth, exit multiple, margins, and reinvestment when QJ does not provide them.

## Required Output

- Inputs table: source each data point or mark as user assumption.
- Scenario table: bear/base/bull where assumptions are visible.
- Sensitivity: at least one key sensitivity when doing DCF or exit multiple work.
- Valuation range: framed as research range, not target-price instruction.
- Open questions: missing peers, stale estimates, incomplete statements.

## Guardrails

- Do not fabricate WACC, terminal growth, share count, debt, cash, or peer multiples.
- Do not turn a valuation range into a buy/sell instruction.
