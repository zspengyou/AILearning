from pyspark import SparkConf, SparkContext

# import os
# os.environ['PYSPARK_PYTHON'] = ""

conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
conf.set("spark.default.parallelism","1")
sc = SparkContext(conf=conf)
print(sc.version)

def add1(input):
    return input + 1

list_rdd = sc.parallelize([1, 2, 3, 4, 5], numSlices=2)
print(f"original collect {list_rdd.collect()}")
rdd3 = list_rdd.map(lambda x: x + 1)
print(f"after map {rdd3.collect()}")
rdd4 = list_rdd.map(add1)
print(f"after map {rdd4.collect()}")

dictionary_rdd = sc.parallelize({"key": "value", "key2": "value2"})
print(f"original collect {dictionary_rdd.collect()}")

# file = sc.textFile(os.path.join(__location__, "__init__.py"))
# print(file.collect())

string_rdd= sc.parallelize(["as ab", "hi jay"])
print(f"flatmap {string_rdd.flatMap(lambda x: x.split(' ')).collect()}")

k_v_rdd = sc.parallelize([('male',1), ('male',2),('female',3), ('female',1)])
print(f"reduceByKey {k_v_rdd.reduceByKey(lambda x,y:x+y).collect()}")

# count frequency of word
from pathlib import Path

test_file = Path(__file__).with_name('test.py')
file_rdd = sc.textFile(str(test_file))
word_rdd = file_rdd.flatMap(lambda x: x.split(" "))
word_with_one = word_rdd.map(lambda word: (word,1))
result_rdd = word_with_one.reduceByKey(lambda a,b: a+b)
print(result_rdd.collect())
sort_rdd = result_rdd.sortBy(lambda tuplit : tuplit[1])
print(sort_rdd.collect())





sc.stop()
