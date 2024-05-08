import os
import logging

from pyspark import SparkContext
#from pyspark.conf import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, FloatType, StringType
from pyspark.sql.functions import expr, column

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("AVIBSparkJob")

# Set environment value for the executors
#os.environ["DISABLE_CERT_CHECKING_SYSTEM_PROPERTY"] = True

#conf = SparkConf()
#conf.set("spark.executorEnv.com.amazonaws.sdk.disableCertChecking", "true")

#spark = SparkSession.builder.config(conf=conf).getOrCreate()

spark = SparkSession.builder.getOrCreate()

def load_config(spark_context: SparkContext):
    spark_context._jsc.hadoopConfiguration().set("fs.s3a.access.key", os.getenv("AWS_ACCESS_KEY_ID", "gl8rbGORHSpxmg1V"))
    spark_context._jsc.hadoopConfiguration().set("fs.s3a.secret.key", os.getenv("AWS_SECRET_ACCESS_KEY", "8WphDMckYqRb29s43SzA4trsV2GgaQRc"))
    spark_context._jsc.hadoopConfiguration().set("fs.s3a.endpoint", os.getenv("ENDPOINT", "gsdpi-hl.default.svc.cluster.local:9000"))
    spark_context._jsc.hadoopConfiguration().set("fs.s3a.connection.ssl.enabled", "true")
    spark_context._jsc.hadoopConfiguration().set("fs.s3a.path.style.access", "true")
    spark_context._jsc.hadoopConfiguration().set("fs.s3a.attempts.maximum", "1")
    spark_context._jsc.hadoopConfiguration().set("fs.s3a.connection.establish.timeout", "5000")
    spark_context._jsc.hadoopConfiguration().set("fs.s3a.connection.timeout", "10000")

load_config(spark.sparkContext)

# Read CSV file from Minio
df = spark.read.option("header", "true").option("inferSchema", "true").csv("s3a://65cd021098d02623c46da92d/65cd02d9e6ba3947be825ac8/66085488056b08fae55840e5/gen_datamatrix.csv")

# Filter dataframe by annotation column name
annotation_df = df.select(column(df.columns[0]).alias("sample_id"), column("HIF3A").alias("expression"))

# show annotation spark dataframe result
annotation_df.show()
