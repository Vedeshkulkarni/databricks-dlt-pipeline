import dlt

#ingestion of data from bronze volume new table
#cuostomers table
@dlt.table(
    name="customers_bronze"
)
def customers_bronze():
    df=spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format", "csv")\
            .load("/Volumes/databricksvedesh/bronze/bronze_volume/customers/")
    return df 
  
#products table
@dlt.table(
    name="products_bronze"
)
def products_bronze():
    df=spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format", "csv")\
            .load("/Volumes/databricksvedesh/bronze/bronze_volume/products/")
    return df 
  
#sales table
@dlt.table(
    name="sales_bronze"
)
def sales_bronze():
    df=spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format", "csv")\
            .load("/Volumes/databricksvedesh/bronze/bronze_volume/sales/")
    return df   
  
#stores table
@dlt.table(
    name="stores_bronze"
)
def stores_bronze():
    df=spark.readStream.format("cloudFiles")\
        .option("cloudFiles.format", "csv")\
            .load("/Volumes/databricksvedesh/bronze/bronze_volume/stores/")
    return df 

