"""Fabric PySpark notebook source; requires Fabric Spark and an attached Lakehouse.
Place synthetic transactions.csv at Files/raw/transactions.csv before running.
"""
from pyspark.sql import functions as F
raw = spark.read.option("header", True).csv("Files/raw/transactions.csv")
needed = {"transaction_id","customer_id","amount","hour","is_international","is_new_device","chargeback","merchant_category","country"}
if not needed.issubset(set(raw.columns)):
    raise ValueError("Missing columns: "+str(needed-set(raw.columns)))
df = (raw.withColumn("amount",F.col("amount").cast("double"))
 .withColumn("hour",F.col("hour").cast("int"))
 .withColumn("is_international",F.col("is_international").cast("int"))
 .withColumn("is_new_device",F.col("is_new_device").cast("int"))
 .withColumn("chargeback",F.col("chargeback").cast("int")))
valid=(F.col("transaction_id").isNotNull() & F.col("customer_id").isNotNull() &
 F.col("amount").isNotNull() & (F.col("amount")>=0) & F.col("hour").between(0,23) &
 F.col("is_international").isin(0,1) & F.col("is_new_device").isin(0,1) &
 F.col("chargeback").isin(0,1))
if df.filter(~F.coalesce(valid,F.lit(False))).limit(1).count():
    raise ValueError("Invalid rows found; quarantine and inspect before loading")
if df.groupBy("transaction_id").count().filter("count > 1").limit(1).count():
    raise ValueError("Duplicate transaction_id")
df=(df.withColumn("risk_score",F.when(F.col("amount")>=1500,2).otherwise(0)
 +F.when(F.col("hour").between(0,5),1).otherwise(0)
 +F.col("is_international")+2*F.col("is_new_device"))
 .withColumn("review_flag",(F.col("risk_score")>=4).cast("int")))
# Full snapshot overwrite; incremental loads require an upsert strategy.
df.write.format("delta").mode("overwrite").option("overwriteSchema","true").saveAsTable("curated_transactions")
print("Curated rows:",df.count())
