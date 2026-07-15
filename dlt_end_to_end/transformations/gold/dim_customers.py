import dlt
from pyspark.sql.functions import *

#creating gold streaming view on top of silver streaming view

@dlt.view(
    name= "products_gold_view"
)
def products_gold_views():
    df=spark.readStream.table("products_silver_view")
    return df

#creating fact table(using atto cdc)
dlt.create_streaming_table(
    name="dim_products"
)
dlt.create_auto_cdc_flow(
    target="dim_products",
    source="products_gold_view",
    keys=["product_id"],
    sequence_by=col("processdate"),
    except_column_list=["processdate"],
    stored_as_scd_type=2
)


 