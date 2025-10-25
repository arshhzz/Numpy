import numpy as np

# arr = np.array([1, 2, 3, np.nan, 5, np.nan])
# print(np.isnan(arr))  ## to detect nan values

# cleaned_arr = np.nan_to_num(arr, nan = -1) ## to replace those with some numbers
# print(cleaned_arr)

# np.isinf() # this one is used to detect infinite values like 10 ^ 199999 or 1/0

arr = np.array([1, 3, np.inf, 7, np.inf, 7])
print(arr)

print(np.isinf(arr))

cleaned_arr = np.nan_to_num(arr, posinf=-1)
print(cleaned_arr)





