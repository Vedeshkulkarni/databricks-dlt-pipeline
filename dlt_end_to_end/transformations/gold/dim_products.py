import dlt
from pyspark.sql.functions import *

#creating gold streaming view on top of silver streaming view

@dlt.view(
    name= "customers_gold_view"
)
def customers_gold_views():
    df=spark.readStream.table("customers_silver_view")
    return df

#creating fact table(using atto cdc)
dlt.create_streaming_table(
    name="dim_customers"
)
dlt.create_auto_cdc_flow(
    target="dim_customers",
    source="customers_gold_view",
    keys=["customer_id"],
    sequence_by=col("processdate"),
    except_column_list=["processdate"],
    stored_as_scd_type=2
)


 