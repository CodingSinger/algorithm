import time
import timeit

start = time.time()

time.sleep(2)

print(time.time()-start)
start1 = time.clock()

time.sleep(2)
print(time.clock()-start1)

start2 = timeit.default_timer()
time.sleep(3)

print(timeit.default_timer()-start2)