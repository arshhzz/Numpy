import numpy as np
arr = np.array([2, 4, 6, 8, 10, 12, 14])

# print(arr[-1]) # negaive index, so picks the element from the back of the array

# print(arr[0]) # selects only first one

# print(arr[0:]) # starts from zero goes till the last element

# print(arr[:4]) #starts from 0th and goes upto 3 (inclusive)

# print(arr[::2]) #moves with the step of two

# print(arr[[0, 2, 4]]) #gives selective indices aka FANCY INDEXING (picking up multiple elements using a list of indices)

## filtering data

## boolean masking

# print(arr[arr > 5]) # so this will bring me the elements from the 'arr' that are above 5

