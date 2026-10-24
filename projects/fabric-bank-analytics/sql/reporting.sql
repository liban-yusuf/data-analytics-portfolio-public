-- Read-only query in the Fabric Lakehouse SQL analytics endpoint.
SELECT merchant_category, COUNT(*) AS transactions,
SUM(review_flag) AS alerts, SUM(chargeback) AS chargebacks,
CAST(100.0*SUM(review_flag)/NULLIF(COUNT(*),0) AS decimal(10,2)) AS alert_pct
FROM curated_transactions GROUP BY merchant_category ORDER BY transactions DESC;
SELECT SUM(CASE WHEN review_flag=1 AND chargeback=1 THEN 1 ELSE 0 END) AS true_positives,
SUM(CASE WHEN review_flag=1 AND chargeback=0 THEN 1 ELSE 0 END) AS false_positives,
SUM(CASE WHEN review_flag=0 AND chargeback=1 THEN 1 ELSE 0 END) AS false_negatives
FROM curated_transactions;
