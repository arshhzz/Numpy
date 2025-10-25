import numpy as np

'''
So basically the insert helps us to modify array
by making a copy of that altering that copy
it doesnt change the og, we can although reassign it

np.insert(a, b, c, d)
a = name of the arr
b = index or positioning where you want to insert
c = data/value that you want to insert
d = axis(not for 1d) = 0 -> row wise , 1 -> column wise 
'''

# arr = np.array([1, 2, 3, 4, 5, 6]) 
# print(arr)

# arr_mod = np.insert(arr, 1, 0) #this will create a copy with the modification, as the arrays cant be changed when it comes to their length
# print(arr_mod)

# arr = np.array([[1, 2], [3, 4]])
# print(arr)

# arr_mod_2d = np.insert(arr, 1, [0, 0], 1)
# print(arr_mod_2d)


## APPEND, similar to insert here also a copy is created

# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# new_arr = np.append(arr, 6)
# print(new_arr)

## concatenation

'''
concatenation(arr1, arr2, axis)
axis 0 > vertical stacking
axis 1 > horizontal stacking
'''

# arr1 = np.array([1, 2, 3, 4, 5])
# print(arr1)
# arr2 = np.array([5, 4, 3, 2, 1])
# print(arr2)
# newarr = np.concatenate((arr1, arr2))
# print(newarr)


## REMOVING ELEMENTS OF ARRAY
'''
np.delete(array, index, axis = None) // none -> flattened array se delete kr rhe
'''

arr = np.array([1, 2, 3, 4, 5])
print(arr)
arr_mod = np.delete(arr, 0)
print(arr_mod)