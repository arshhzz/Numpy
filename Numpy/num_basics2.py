#AGGREGATION FUNCTIONS IN NUMPY
import numpy as np

#sum , mean, median, std, var, min, max

arr = np.array([1, 2, 3, 4, 5])

print("Original Array:", arr)
print("sum: ", np.sum(arr)) # computes the sum of all elements in the array
print("mean: ", np.mean(arr)) # computes the mean (average) of the array elements
print("median: ", np.median(arr))   # computes the median value of the array elements
print("std: ", np.std(arr)) # computes the standard deviation of the array elements
print("var: ", np.var(arr)) # computes the variance of the array elements
print("min: ", np.min(arr)) # computes the minimum value among the array elements
print("max: ", np.max(arr)) # computes the maximum value among the array elements
# Each function computes the respective aggregation on the array elements.
