# QJ MCP Tool Map

Use `data.*` tools as the primary source. Use `api.domains.call` only for missing raw data.

## Core Company Data

- Identity and coverage: `data.instruments.search`, `data.coverage.ticker`, `data.coverage.catalog`
- Company profile: `data.profile.get`, `data.profile.search`, `data.profile.batch`
- Composite research packet: `data.ticker.deep_dive`

## Market Data

- Latest price: `data.prices.latest`
- Return windows: `data.prices.returns`
- History: `data.prices.history`
- Batch prices: `data.prices.batch`
- Benchmarks: `data.benchmarks.indices`, `data.benchmarks.quotes`, `data.benchmarks.compare`

## Fundamentals and Metrics

- Statements: `data.fundamentals.statements`, `data.fundamentals.latest`, `data.fundamentals.pit`
- Fields: `data.fundamentals.fields`, `data.fundamentals.field_series`
- Metrics: `data.metrics.snapshot`, `data.metrics.history`, `data.metrics.trends`, `data.metrics.technicals`
- Screening: `data.metrics.screen`, `data.metrics.rank`, `data.metrics.universe`

## Estimates and Earnings

- Consensus: `data.estimates.consensus`
- Surprise: `data.estimates.surprise`
- Grades and targets: `data.estimates.grades`, `data.estimates.targets`
- Revisions and dispersion: `data.estimates.revisions`, `data.estimates.dispersion`
- Events: `data.events.earnings_calendar`, `data.events.consensus_drift`

## Events and Catalysts

- Dividends and splits: `data.events.ticker_dividends`, `data.events.ticker_splits`
- Macro events: `data.events.macro_calendar`
- Unified calendar: `data.events.calendar_all`
- Portfolio event exposure: `data.events.exposure_summary`, `data.events.risk_summary`

## Ownership and Flows

- Institutional holders: `data.institutional.holders`, `data.institutional.history`, `data.institutional.top_holders`
- 13F: `data.sec13f.ownership_search`, `data.sec13f.ownership_ticker`, `data.sec13f.ownership_fund`

## Government and Political Signals

- Congress: `data.congress.summary`, `data.congress.transactions`, `data.congress.trade_signals`
- Government contracts: `data.gov.summary`, `data.gov.contract_awards`, `data.gov.contract_signals`

## Portfolio and Risk

- PM brief: `data.intelligence.pm_brief`
- Portfolio: `data.portfolio.tree`, `data.portfolio.dashboard`, `data.portfolio.holdings`, `data.portfolio.positions`, `data.portfolio.nav`, `data.portfolio.pnl`, `data.portfolio.attribution`
- Risk: `data.risk.info`, `data.risk.scenario_list`, `data.risk.scenario_run`, `data.risk.hedge_suggestions`, `data.risk.factor_exposure`

## Fallback Raw API

Use `api.domains.describe_route` before calling unfamiliar routes. Use `api.domains.call` for raw domain routes when `data.*` is missing or stale. Record fallback usage under `Coverage`.
