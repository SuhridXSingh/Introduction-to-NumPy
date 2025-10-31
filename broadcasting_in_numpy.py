import numpy as np

array1 = np.array([[1,2,3,4]]) #one row of 4 columns (1,4)
array2 = np.array([[1],[2],[3],[4]]) #4 rows of 1 column (4,1)

print(array1.shape)# (1,4)
print(array2.shape)# (4,1)

#Boradcasting:

print(array1 * array2)

array3 = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

#array3 can be broadcasted with both array1 and array 2 as array3 shape is (4,4).

print(array1*array3)
