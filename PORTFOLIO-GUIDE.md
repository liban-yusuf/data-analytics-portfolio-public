# Portfolio reading guide

This portfolio groups work by business problem rather than by programming language. All example datasets are synthetic unless explicitly stated otherwise.

## 1 — Financial risk
[Bank Fraud Detection](projects/bank-fraud/README.md): transparent transaction triage using SQLite, Python, and unit tests. Start with the business question, then inspect the scoring rules, run the script, and explain false positives versus missed cases.

## 2 — Customer and commercial analytics
- [Customer Sales Analysis](https://github.com/libana3012-pixel/Customer-Sales-Analysis): joins, customer segmentation and repeat purchase.
- [Sales Revenue Analysis](https://github.com/libana3012-pixel/Sales-Revenue-Analysis): sales KPIs and reconciliation.
- [Customer Cohorts](projects/customer-cohorts/README.md): retention-window logic.

## 3 — Data reliability
- [Data Quality](projects/data-quality/README.md): detect inconsistent source records.
- [Python Sales Cross-check](python/README.md): independently verify reported figures.

## 4 — Marketing analytics
[Marketing Analytics Portfolio](https://github.com/libana3012-pixel/Marketing-Analytics-Portfolio): measurement planning, campaign metrics, and organic search.

## 5 — Microsoft Fabric (planned)
[Fabric Bank Transaction Analytics blueprint](projects/fabric-bank-analytics/README.md): proposed ingestion pipeline, Lakehouse structure, SQL transformations and Power BI report. **Design only; not deployed or tested in Fabric.**

## Recommended review order
1. Read each README's business question and conclusions.
2. Run the source code and tests where available.
3. Explain assumptions, data limitations and what the next iteration should test.
4. Keep a clear distinction between implemented work and future plans.

## Repository organization policy
The public portfolio is the entry point; the dedicated customer, revenue and marketing repositories retain their own code and history. No existing repository has been deleted, archived or renamed.
