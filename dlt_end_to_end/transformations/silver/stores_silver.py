import dlt 
from pyspark.sql.functions import *

@dlt.view(
    name="stores_silver_view"
)
def stores_silver_view():
    df_str = spark.readStream.table("stores_bronze")
    #transformation
    df_str=df_str.withColumn("processdate",regexp_replace(col("store_name"),"_",""))
    df_str=df_str.withColumn("processdate", current_timestamp())
    return df_str

#stores silver with upsert
dlt.create_streaming_table(
    name="stores_silver"
)
dlt.create_auto_cdc_flow(
    target="stores_silver",
    source="stores_silver_view",
    keys=["store_id"],
    sequence_by=col("processdate"),
    stored_as_scd_type=1
)

    