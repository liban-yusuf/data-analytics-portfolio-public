# ETL Data Validation & Reconciliation

**Status:** executable local learning exercise, synthetic data only.

## Business question
Reject duplicates and invalid amounts; reconcile accepted rows and revenue.

## Run
From the repository root:
```bash
python3 projects/etl-data-validation/analyze.py
```

## Skills demonstrated
ETL checks, duplicate handling, Decimal arithmetic, reconciliation and deterministic assertions.

## Limitations
The small fabricated dataset illustrates logic, not production performance.

## Interview prompt
Explain the business trade-off, how you validated the numbers, and what you would improve with real-world data.
