import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

#array[start:end:step]

print(array[0:3]) #First 3 rows will be printed.
print(array[0::2]) #0th and 2nd index rows will be printed.
print(array[::-1]) #All the rows but reversed.

#To select columns :
print(array[:,0]) #0th index column
print(array[:,1]) #1st index column
print(array[:,0:3]) #All columns from 0-2nd index.
print(array[0:3,0:3]) # 3 by 3 matrix.
print(array[1:3,1:3]) # 2 by 2 matrix at the centre.
print(array[0:2,2:]) #2 by 2 matrix at the top right.
