import numpy as np

rng = np.random.default_rng() #A Random Number generator.

print(rng.integers(1,7)) #A Dice (output as a 0D array)

print(rng.integers(low=1,high=101,size=3)) #output as a 1D array
print(rng.integers(low=1,high=101,size=(3,3))) #output as a 2D array (Selects a random Matrix)
print(rng.integers(low=1,high=101,size=(3,3,3))) #output as a 3D array

#Generate random float:

print(np.random.uniform())
print(np.random.uniform(-1,1))
print(np.random.uniform(-1,1,(2,3)))

#Shuffle an array:

array = np.array([1,2,3,4,5])

rng.shuffle(array) 
print(array) #array will be in random order

#Random Choice:

fruits = np.array(['apple','orange','banana','guava'])

fruit = rng.choice(fruits,size = 2)
print(fruit) #chooses a random fruit from the array
