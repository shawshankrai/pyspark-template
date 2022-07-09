from sparkutils import get_spark_session

def handler():
    spark = get_spark_session()
    sum_of_range = spark.range(10000).where('id > 1000').selectExpr('sum(id)').collect()
    print(sum_of_range)