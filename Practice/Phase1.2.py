import numpy as np

arr = np.arange(1, 10).reshape(3, 3)
print(arr)

temp = np.arange(1, 4).reshape(3, 1)
print(temp)

res = arr + temp
print(res)