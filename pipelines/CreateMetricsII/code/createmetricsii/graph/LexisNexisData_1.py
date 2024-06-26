from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from createmetricsii.config.ConfigStore import *
from createmetricsii.udfs.UDFs import *

def LexisNexisData_1(spark: SparkSession) -> DataFrame:
    return spark.read.table("`lineage_data.default`.`LexisNexisData`")
