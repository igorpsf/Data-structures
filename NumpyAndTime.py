import time
import numpy as np

x = np.random.random(10000000) # 10 mln

start = time.time()
sum(x) / len(x)
print(time.time() - start)

start = time.time()
np.mean(x)
print(time.time() - start)

a = np.array([1, 2, 3, 4, 5])
print(a)