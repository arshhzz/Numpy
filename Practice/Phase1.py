import numpy as np

arr = np.arange(1, 37).reshape(6, 6)
print(arr)

arr_reshape = arr.reshape(3, 3, 4)
print(arr_reshape)

arr_back = arr_reshape.reshape(6, 6)
print(arr_back)

print("Data Integrity:", np.array_equal(arr, arr_back))

arr_flatten_one = arr.ravel()
print("The flattened array: ", arr_flatten_one)
