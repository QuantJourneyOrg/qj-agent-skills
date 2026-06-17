---
name: qj-congress-gov-signals
description: QJ MCP-backed political and government-contract signal workflow. Use when the user asks about Congress trades, politician transactions, government awards, public-sector contract signals, policy-linked tickers, or portfolio exposure to government and political activity.
---

# QJ Congress Gov Signals

Analyze government and congressional signals without treating them as standalone trade signals.

## Workflow

1. Pull data-plane status with `data.congress.summary` and `data.gov.summary`.
2. For ticker analysis, pull `data.congress.trade_signals`, `data.congress.transactions`, `data.gov.contract_signals`, and `data.gov.contract_awards`.
3. Add company context with `data.profile.get`, `data.metrics.snapshot`, and `data.prices.returns`.
4. For portfolio context, add `data.portfolio.holdings_by_ticker` and `data.events.exposure_summary`.
5. Use fallback `api.domains.call` only for missing raw market context.

## Required Output

- Signal inventory: transactions, awards, direction, dates, and confidence if provided.
- Materiality view: connect signals to company size, revenue context, or sector exposure when available.
- False-positive risks: lag, disclosure timing, immaterial awards, unrelated tickers.
- Monitoring triggers.

## Guardrails

- Do not present government or Congress activity as causal proof.
- Always separate signal from investment conclusion.
