---
name: qj-equity-deep-dive
description: Full QJ MCP-backed public equity research workflow for a single stock or small ticker set. Use when the user asks for a deep dive, company analysis, investment research note, stock review, quality/growth/value/risk read, or source-backed thesis using QuantJourney data.
---

# QJ Equity Deep Dive

Use QJ MCP tools to build a concise, evidence-backed company research note.

## Workflow

1. Resolve the ticker with `data.instruments.search` when identity is ambiguous.
2. Check coverage with `data.coverage.ticker`.
3. Pull the base packet with `data.ticker.deep_dive`.
4. Fill gaps with `data.profile.get`, `data.prices.*`, `data.fundamentals.latest`, `data.metrics.snapshot`, `data.metrics.trends`, `data.estimates.*`, `data.events.*`, `data.institutional.holders`, and `data.sec13f.ownership_ticker`.
5. Use `api.domains.describe_route` and `api.domains.call` only when a required field is missing from `data.*`.
6. Produce the output contract from `../../shared/references/output-contract.md`.

## Analysis Frame

- Business: what the company does, segments if available, and current market context.
- Fundamentals: revenue/profit/cash-flow trend, balance-sheet quality, margins, and returns.
- Valuation: current multiples and estimate context; defer full modeling to `qj-valuation-workbench`.
- Events: upcoming earnings, dividends, splits, macro or corporate events.
- Ownership: institutional and 13F context when available.
- Risks: data gaps, deterioration signals, estimate dispersion, concentration, and event risk.

## Required Guardrails

- Read `../../shared/references/evidence-standard.md` when producing a formal note.
- Read `../../shared/references/compliance-boundaries.md` when the user asks what to do with the stock.
- Do not issue trade instructions.
- Mark missing data under `Coverage`.
