import numpy as np

arr = np.random.randint(-20, 20, 10)
print(arr)

neg_mask = arr < 0

arr[neg_mask] = 0

print(arr) # boolean maskeddd


arr = np.random.randint(0, 100, 30)
print(arr)

onlyThreeAndFive = ((arr % 3 == 0) & (arr % 5 == 0))
print(arr[onlyThreeAndFive])

