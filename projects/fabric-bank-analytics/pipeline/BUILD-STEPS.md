# Data Factory pipeline — manual build instructions
**Not deployed.** In a Fabric-capacity workspace:
1. Create a Lakehouse named `bank_analytics`.
2. Upload the synthetic `projects/bank-fraud/transactions.csv` to `Files/raw/transactions.csv` for a first manual run.
3. Create a Data Factory pipeline named `pl_bank_ingestion`. For automated ingestion, configure Copy Data from a permitted source into the Lakehouse Files raw landing zone.
4. Add a Notebook activity pointing to `notebooks/curate_transactions.py` copied into a Fabric notebook attached to the Lakehouse. Use activity dependency success/failure branches.
5. Run manually and verify the curated Delta table, row counts and duplicate checks.
6. Run `sql/reporting.sql` using the read-only SQL analytics endpoint.
7. Build the semantic model and report using `powerbi/MEASURES.md`.
8. Capture redacted screenshots and execution timestamps before marking any Fabric step complete.

Note: the notebook uses full-snapshot overwrite; do not schedule incremental append loads until idempotent merge behavior is implemented.
