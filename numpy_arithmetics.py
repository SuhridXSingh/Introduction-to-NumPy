import numpy as np

#Scalar arithmetic

array = np.array([1,2,3])

array+=1
print(array) # 1 added to each element
array -= 2
print(array) # 2 subtracted from current array
array +=2
array-=1
print(array) #old array
print(array*3)

#Vectorized math Functions:

print(np.sqrt(array))

array_1 = np.array([1.02 , 2.5 , 3.99])

print(np.round(array_1))

print(np.pi)

#Example exercise:

radii = np.array([2,3,4])

area = np.pi * (radii**2)

print(area)

#Element-wise arithmetic:

print(array + array_1) 
print(array - array_1) 
print(array * array_1) 
print(array / array_1) 
print(array ** array_1) 

#Comparison operators: (element-wise comparison)

scores = np.array([99,100,35,66,89,78,92,35,55,47,72])
print(scores==100) #If someone got 100 or not
print(scores>=60) #Passed students

scores[scores<60]=0
scores[scores>=60]=1
print(scores)
