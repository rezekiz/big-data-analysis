"""

====================================================
#                                                  #
#    Data preprocessing using (Py)Spark            #
#    These scripts use the files located on the    #
#    datasets folder on the repo root              #
#                                                  #
====================================================


"""

# Import required libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col


# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Pandas to PySpark") \
    .getOrCreate()

# Load datasets
pop = spark.read.csv('../datasets/raw/population.csv', header=True)
obes = spark.read.csv('../datasets/raw/share-of-adults-defined-as-obese.csv', header=True)
mental = spark.read.csv('../datasets/raw/mental-illnesses-prevalence.csv', header=True)


# Rename columns
pop = pop.withColumnRenamed('Entity', 'Country')
obes = obes.withColumnRenamed('Entity', 'Country')
mental = mental.withColumnRenamed('Entity', 'Country')

# Filter datasets
pop = pop.filter((col('Year') >= 1990) & (col('Year') <= 2016))
obes = obes.filter((col('Year') >= 1990) & (col('Year') <= 2016))
mental = mental.filter((col('Year') >= 1990) & (col('Year') <= 2016))

# Merge datasets
fused = pop.join(obes, ['Country', 'Year'], 'inner') \
    .join(mental, ['Country', 'Year'], 'inner')

# Drop rows with null values
fused = fused.dropna()

# Export to CSV
fused.coalesce(1).write.option("header", "true").csv('../datasets/processed/spark_processed_data.csv')

# Stop SparkSession
spark.stop()