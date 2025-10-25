import numpy as np 

"""
reshape(rows, columns) specify new shape
if dimensions match only then
"""

# arr = np.array([2, 4, 6, 8, 10, 12])
# reshaped_arr = arr.reshape(2, 3) # this will run as the 2 x 3 results in 6 elements so it satisfies the dimensions

# reshaped_arr = arr.reshape(2, 2) # this will fail for the 'arr' array as the elements contradict the dimensions

# print(reshaped_arr)


# arr = np.array([2, 4, 6, 8, 10, 12])
# arr = arr.reshape(2, 3)
# print(arr)
# print(type(arr))
# print(arr.ndim)

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# flatten_arr = arr.ravel()

# print(flatten_arr)
# flatten_arr[0] = 5
# print(arr) # so ravel is more efficient but it can makes a refernece copy to work on, when you make changes to the copy, it will reflect
            # on the original copy

arr = np.array([[1, 2, 3], [4, 5, 6]])
flatten_arr = arr.flatten()
flatten_arr[0] = 5
print(flatten_arr)

