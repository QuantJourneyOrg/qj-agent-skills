---
name: qj-earnings-preview
description: QJ MCP-backed pre-earnings research workflow. Use when the user asks for an earnings preview, setup before results, key debates, consensus expectations, estimate revisions, management questions, or event risk before a company reports.
---

# QJ Earnings Preview

Prepare a pre-earnings setup without predicting the result.

## Workflow

1. Confirm the ticker and next event with `data.events.earnings_calendar`.
2. Pull expectations with `data.estimates.consensus`, `data.estimates.revisions`, `data.estimates.dispersion`, and `data.estimates.targets`.
3. Review history with `data.estimates.surprise`, `data.events.consensus_drift`, `data.metrics.trends`, and `data.fundamentals.latest`.
4. Add market context with `data.prices.returns` and `data.metrics.snapshot`.
5. Use `api.domains.call` only when the curated estimate or event fields are missing.

## Required Output

- Expectations: consensus, revisions, dispersion, and recent drift.
- Historical pattern: beat/miss and post-earnings context when available.
- Key debates: 3-5 questions that results should answer.
- Watch items: metrics, guidance items, margin points, demand indicators.
- Open questions and data gaps.

## Guardrails

- Do not forecast a beat or miss without evidence.
- Label all qualitative debate points as interpretation.
- Use the shared output contract for formal previews.
