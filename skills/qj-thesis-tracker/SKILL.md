---
name: qj-thesis-tracker
description: QJ MCP-backed living thesis workflow. Use when the user wants to create, update, audit, or monitor an investment thesis, assumptions, catalysts, risks, evidence changes, and review triggers for a ticker or watchlist.
---

# QJ Thesis Tracker

Turn research into a monitored thesis file.

## Workflow

1. Capture the user's thesis, time horizon, and current assumptions.
2. Pull current facts with `data.ticker.deep_dive`, `data.metrics.snapshot`, `data.estimates.*`, `data.events.calendar_all`, and `data.institutional.*`.
3. Identify catalysts with `data.events.*`, `data.gov.contract_signals`, and `data.congress.trade_signals` when relevant.
4. Create or update the thesis table from `../../shared/templates/thesis-tracker.md`.
5. Add review triggers: metric thresholds, estimate changes, event dates, ownership changes, or risk flags.

## Required Output

- Thesis summary.
- Core assumptions.
- Evidence supporting and evidence against.
- Catalysts and dated triggers.
- Review rules and open questions.
- Tools used.

## Guardrails

- Do not rewrite a user thesis into a recommendation.
- Preserve contradictory evidence.
- Mark user assumptions separately from QJ-sourced facts.
