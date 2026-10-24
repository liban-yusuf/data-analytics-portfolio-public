# Liban Yusuf | Data Analytics Portfolio

[Complete project workflow](WORKFLOW.md)

[How the work was carried out, with tools and calculations](WORKFLOW.md)
### SQL · Python · Data Quality · Business Intelligence

[![Portfolio checks](https://github.com/liban-yusuf/data-analytics-portfolio-public/actions/workflows/verify.yml/badge.svg)](https://github.com/liban-yusuf/data-analytics-portfolio-public/actions/workflows/verify.yml)

**Technical learning chapter: April–October 2026** · [Previous chapter: Marketing Analytics](https://github.com/liban-yusuf/Marketing-Analytics-Portfolio)

## About me
I'm Liban Yusuf, based in Oslo, with a bachelor's degree in Marketing and Sales Management and experience with digital analytics and business reporting. My interest is in turning business questions into reliable numbers: defining the question, preparing data, checking the result and communicating findings clearly.

This collection shows my technical progression after the marketing-focused learning chapter. The example datasets are **synthetic**. The dates in a dataset and the thematic chapter dates do not represent historical upload dates, employment outcomes or invented certification claims.

[**Portfolio reading guide — start here**](PORTFOLIO-GUIDE.md)

## Portfolio organization

**Featured standalone repositories:** [Customer Sales Analysis](https://github.com/liban-yusuf/Customer-Sales-Analysis) · [Sales Revenue Analysis](https://github.com/liban-yusuf/Sales-Revenue-Analysis) · [Marketing Analytics Portfolio](https://github.com/liban-yusuf/Marketing-Analytics-Portfolio)

**Projects currently hosted inside this repository:** [Bank Fraud Detection](https://github.com/liban-yusuf/bank-fraud-analysis) · [Fabric Bank Analytics (implementation source, not deployed)](https://github.com/liban-yusuf/microsoft-fabric-bank-analytics) · [Analytics mini-projects](PORTFOLIO-GUIDE.md).

**Separate repositories:** [Bank Fraud Analysis](https://github.com/liban-yusuf/bank-fraud-analysis), [Microsoft Fabric Bank Analytics](https://github.com/liban-yusuf/microsoft-fabric-bank-analytics), and [Analytics Mini Projects](https://github.com/liban-yusuf/analytics-mini-projects). Original project files remain in this repository as an archive; no files have been deleted.

## Featured project — Financial Risk

[**Bank Fraud Detection (SQL + Python)**](https://github.com/liban-yusuf/bank-fraud-analysis): synthetic transaction risk scoring, chargeback proxy evaluation and automated tests. This is a reproducible learning exercise, not a production fraud system.

## Browse by skill

| Category | Projects |
| --- | --- |
| Financial risk | [Bank Fraud Detection](https://github.com/liban-yusuf/bank-fraud-analysis) |
| SQL & business analysis | [Customer Sales Analysis](https://github.com/liban-yusuf/Customer-Sales-Analysis), [Sales Revenue Analysis](https://github.com/liban-yusuf/Sales-Revenue-Analysis) |
| Python & data quality | [Customer cohorts](projects/customer-cohorts/README.md), [Data quality](projects/data-quality/README.md), [Sales verification](python/README.md) |
| Marketing analytics | [Marketing Analytics Portfolio](https://github.com/liban-yusuf/Marketing-Analytics-Portfolio) |
| Microsoft Fabric | [Bank analytics build blueprint](https://github.com/liban-yusuf/microsoft-fabric-bank-analytics) — planned, not deployed |

## Focused technical mini-projects

These short, runnable exercises complement the larger case studies and demonstrate specific analyst skills.

| Mini-project | Skill | Evidence |
| --- | --- | --- |
| [SQL Window Functions & KPI Trends](https://github.com/liban-yusuf/analytics-mini-projects/tree/main/sql-window-kpis) | LAG, running totals, month-over-month KPIs | SQLite script and assertions |
| [ETL Data Validation](https://github.com/liban-yusuf/analytics-mini-projects/tree/main/etl-data-validation) | Duplicates, invalid records, reconciliation | Python validation script |
| [Fraud Threshold Evaluation](https://github.com/liban-yusuf/analytics-mini-projects/tree/main/fraud-threshold-evaluation) | Precision, recall, alert-volume trade-offs | Synthetic threshold comparison |

## Where to start
| Study | Business question | Evidence |
| --- | --- | --- |
| [Sales Revenue Analysis](https://github.com/liban-yusuf/Sales-Revenue-Analysis) | Why did sales value change? | SQL, modelling, KPIs and automated checks |
| [Customer Sales Analysis](https://github.com/liban-yusuf/Customer-Sales-Analysis) | Who purchased, returned or never ordered? | SQL, segmentation and automated checks |
| [Customer cohorts](projects/customer-cohorts/README.md) | What share of new customers return next month? | Python, transparent follow-up windows |
| [Data quality](projects/data-quality/README.md) | Can problematic source rows be caught before reporting? | Python validation, tests, error fixtures |
| [Sales cross-check](python/README.md) | Do two calculation methods agree? | Independent Python check on synthetic transactions |

[Start here: reading guide](START-HERE.md) · [Skills and project status](SKILLS.md) · [Learning path](LEARNING-PATH.md) · [Development timeline](PROGRESS.md)

## Example findings

- The retail exercise contains **12 orders**, **19 order lines** and **2,020 fictional currency units** in gross line value.
- The customer exercise keeps the one registered customer with no purchases visible by starting from the customer table.
- The cohort exercise does **not** turn missing July follow-up data into a misleading zero-retention result.
- The data-quality exercise intentionally includes broken input to demonstrate detection, not just successful processing.

These are exercises, not real client outcomes.

## How I connect the tools
```text
Business question → relational data / SQL → Python checks
                → reliable KPI definitions → management reporting
                                    → Power BI / Fabric (planned builds)
```

| Area | Tools | Status |
| --- | --- | --- |
| SQL | SQLite, joins, aggregations, window functions | Reproducible public cases |
| Python | CSV, cohort logic, reconciliation, unittest | Source code and tests included |
| Data quality | Duplicate detection, reference/value checks, CI | Automated workflow included |
| Power BI / DAX / Power Query | [Implementation plan](powerbi/README.md) | Draft design; no completed PBIX claimed |
| Microsoft Fabric | [Architecture plan](fabric/README.md) | Proposed future build; not deployed |
| Earlier business background | GA4, GTM, SEO, Excel | [Marketing Analytics chapter](https://github.com/liban-yusuf/Marketing-Analytics-Portfolio) |

## Reproduce the Python exercises
Python 3 is sufficient; no paid service or additional package is required.

```bash
python3 projects/customer-cohorts/cohorts.py
python3 projects/data-quality/check_data.py
python3 -m unittest discover -s projects/data-quality -p 'test_*.py' -v
python3 python/verify_sales.py
```

The deliberately faulty data-quality input is expected to fail if run separately. [Learn how to interpret it](projects/data-quality/README.md).

## Privacy and provenance
All datasets in the published exercises are synthetic. Design documents are marked as plans, not completed deployments; Power BI files and certifications will be added only when available and verified.

*Business questions first. Traceable numbers. Clear decisions.*
