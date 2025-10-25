import numpy as np

arr = np.arange(1, 101).reshape(10, 10)
print(arr)

for i in range(0, 10, 2):
  print(arr[i])

for i in range(0, 10, 1):
  print(arr[i][i])

subamt = arr[2:6, 4:9]
print(subamt)