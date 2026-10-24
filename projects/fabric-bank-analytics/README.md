# Microsoft Fabric — Bank Transaction Analytics

**Status: project blueprint / not implemented in Microsoft Fabric.** This is a proposed follow-on to the [Bank Fraud Detection SQL + Python exercise](../bank-fraud/README.md).

## Business objective
Build a reproducible reporting flow that ingests synthetic transactions, validates data, scores transactions for manual review, and presents aggregate risk metrics.

## Proposed architecture
```text
Synthetic CSV transactions
       |
       v
Fabric Data Factory pipeline (copy + validation orchestration)
       |
       v
OneLake / Lakehouse Files (raw landing zone)
       |
       v
Notebook or SQL transformation -> Lakehouse Delta tables (curated)
       |
       v
Lakehouse SQL analytics endpoint -> Power BI semantic model -> report
```

## Planned build steps
1. Create a Fabric workspace and Lakehouse.
2. Upload the synthetic `transactions.csv` from the bank-fraud case to the Lakehouse Files area.
3. Build a Data Factory pipeline to copy or ingest the file; record successful and failed runs.
4. Validate schema, duplicate IDs, nulls, amount bounds and hour range. Quarantine invalid records.
5. Create a curated Delta table with transparent risk-score fields. Use a notebook for writes/transforms; query the result using the SQL analytics endpoint.
6. Create Power BI measures for transaction count, flagged share, chargeback proxy share, review precision and recall.
7. Document refresh behavior, data lineage, limitations and evidence from actual Fabric runs.

## Data model
- `raw_transactions`: original fields and ingestion metadata.
- `curated_transactions`: validated fields, calculated risk score, review flag.
- `reporting_metrics`: aggregates by merchant category and review flag.

## Acceptance criteria
- Pipeline run succeeds on the sample data and can be rerun without duplicate transactions.
- Curated row count reconciles to valid source rows.
- Scores match the existing Python baseline.
- Power BI measures agree with SQL aggregates.
- Screenshots, workspace configuration, and refresh evidence are added **only after actual implementation**.

## Scope and caveats
No real financial data, credentials or personally identifying information should be committed. The chargeback field is a proxy outcome, not proof of fraud. This repository currently contains a **design**, not a deployed Fabric workspace, pipeline, Lakehouse or Power BI report.

## Implementation assets added

- [PySpark validation and Delta-table transformation](notebooks/curate_transactions.py) — intended for an attached Fabric notebook
- [Read-only reporting SQL](sql/reporting.sql) — for the Lakehouse SQL analytics endpoint
- [Power BI DAX measures and report specification](powerbi/MEASURES.md)
- [Data Factory pipeline build instructions](pipeline/BUILD-STEPS.md)

**Current status:** code and build instructions published to GitHub. A Fabric workspace, successful pipeline execution, Lakehouse table and interactive Power BI report have **not** been verified or deployed. The repository's GitHub Actions workflow checks local Python exercises, not the Fabric runtime.
