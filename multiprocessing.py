import multiprocessing
import os
from datetime import datetime

def square(n):
    print("Worker process id for {0}: {1}".format(n, os.getpid()))
    return (n * n)


if __name__ == "__main__":
 
    mylist = [i for i in range(1000000)]

    # creating a pool object
    start_time = datetime.now()
    p = multiprocessing.Pool()

    # map list to target function
    result = p.map(square, mylist)
    end_time = datetime.now()

    total_time = end_time - start_time
    print(f"Result = {result} \n and Tota Time = {total_time}")
# the result after running the code
# Total Time in for loop = 0:00:00.135964
# Total Time in multiprocessing = 0:00:12.868279
# so for loop is faster than multiprocessing