import dlt
from pyspark.sql.functions import *

#creating gold streaming view on top of silver streaming view

@dlt.view(
    name= "sales_gold_view"
)
def sales_gold_views():
    df=spark.readStream.table("sales_silver_view")
    return df

#creating fact table(using atto cdc)
dlt.create_streaming_table(
    name="facts_sales"
)
dlt.create_auto_cdc_flow(
    target="facts_sales",
    source="sales_gold_view",
    keys=["sales_id"],
    sequence_by=col("processdate"),
    stored_as_scd_type=1
)


 