# QJ Agent Skills Index

This pack contains 14 QJ-native skills. They are methodology skills, not data connectors.

| Skill | Use for | Primary QJ tools |
| --- | --- | --- |
| `qj-equity-deep-dive` | Full company research note | `data.ticker.deep_dive`, `data.metrics.*`, `data.fundamentals.*` |
| `qj-earnings-preview` | Pre-earnings setup and questions | `data.events.earnings_calendar`, `data.estimates.*` |
| `qj-earnings-recap` | Post-earnings update | `data.estimates.surprise`, `data.events.consensus_drift`, fundamentals |
| `qj-valuation-workbench` | DCF, comps, scenario valuation | `data.metrics.*`, `data.fundamentals.*`, `data.estimates.*` |
| `qj-thesis-tracker` | Living thesis file | `data.ticker.deep_dive`, `data.events.*`, user thesis input |
| `qj-portfolio-monitor` | Portfolio review and event/risk monitor | `data.intelligence.pm_brief`, `data.portfolio.*`, `data.risk.*` |
| `qj-congress-gov-signals` | Congress and government-contract intelligence | `data.congress.*`, `data.gov.*` |
| `qj-institutional-flow` | 13F and ownership flow | `data.institutional.*`, `data.sec13f.*` |
| `qj-macro-regime-brief` | Macro, rates, commodities, benchmark context | `data.events.macro_calendar`, `data.benchmarks.*`, `data.commodities.*` |
| `qj-catalyst-calendar` | Dated events and review triggers | `data.events.*`, `data.coverage.*` |
| `qj-idea-generation` | Screen and source research candidates | `data.metrics.screen`, `data.metrics.rank`, `data.gov.*`, `data.congress.*` |
| `qj-risk-bias-review` | Bias, bear case, and data-quality review | Any prior evidence plus `data.risk.*` when portfolio context exists |
| `qj-portfolio-rebalance-planner` | Drift, concentration, and rebalance planning | `data.portfolio.*`, `data.risk.*`, `data.benchmarks.*` |
| `qj-supply-chain-theme-research` | Thematic supply-chain baskets and chokepoints | `data.profile.*`, `data.gov.contract_awards`, `data.metrics.*` |

Common references:

- `shared/references/qj-mcp-tool-map.md`
- `shared/references/evidence-standard.md`
- `shared/references/output-contract.md`
- `shared/references/compliance-boundaries.md`
