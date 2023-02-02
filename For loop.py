
from datetime import datetime
import multiprocessing
import os

mylist = [i for i in range(1000000)]
result = []
start_time = datetime.now()
for i in mylist:
    result.append(i*i)
end_time = datetime.now()


total_time = end_time - start_time
print(f"Result = {result} \n and Total Time = {total_time}")
# the result after running the code
# Total Time in for loop = 0:00:00.135964
# Total Time in multiprocessing = 0:00:12.868279
# so for loop is faster than multiprocessing
