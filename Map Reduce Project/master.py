from splitter import split_file
from mapper import mapper
from partitioner import partition
from sorter import sort_file
from reducer import reducer

split_file()

mapper("chunk1.txt", "map1.txt")
mapper("chunk2.txt", "map2.txt")

partition()

sort_file("partitions/partition0.txt", "partitions/partition0.txt")
sort_file("partitions/partition1.txt", "partitions/partition1.txt")

open("output/result.txt", "w").close()

reducer("partitions/partition0.txt", "output/result.txt")
reducer("partitions/partition1.txt", "output/result.txt")

print("MapReduce Completed Successfully")