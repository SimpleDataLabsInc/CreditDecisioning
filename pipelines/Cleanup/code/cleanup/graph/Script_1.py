from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from cleanup.config.ConfigStore import *
from cleanup.udfs.UDFs import *

def Script_1(spark: SparkSession):
    dbutils.fs.rm(
        '/Prophecy/sparklearner123@gmail.com/finserv/prophecy/ingest/FICO/TransUnionFICO2018.xml',
        recurse = True
    )
    dbutils.fs.rm(
        '/Prophecy/sparklearner123@gmail.com/finserv/prophecy/ingest/FICO/TransUnionFICO2019.xml',
        recurse = True
    )
    dbutils.fs.rm(
        '/Prophecy/sparklearner123@gmail.com/finserv/prophecy/ingest/FICO/TransUnionFICO2020.xml',
        recurse = True
    )
    dbutils.fs.rm(
        '/Prophecy/sparklearner123@gmail.com/finserv/prophecy/ingest/FICO/TransUnionFICO2021.xml',
        recurse = True
    )
    dbutils.fs.rm('/Prophecy/sparklearner123@gmail.com/finserv/prophecy/ReportSCD1', recurse = True)
    dbutils.fs.rm('/Prophecy/sparklearner123@gmail.com/finserv/prophecy/ReportSCD2', recurse = True)
    dbutils.fs.rm('/Prophecy/sparklearner123@gmail.com/finserv/prophecy/ReportSCD3', recurse = True)

    return 
