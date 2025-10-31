import numpy as np

array = np.array ([[1,2,3,4,5],[6,7,8,9,10]])
print(np.sum(array)) #55
print(np.mean(array)) #5.5
print(np.std(array)) #2.87
print(np.var(array)) #8.25
print(np.min(array)) #1
print(np.max(array)) #10
print(np.argmax(array)) #9 (index of max value)(2D array is flattened into 1D array before giving the index)
print(np.sum(array,axis=0)) #sum of columns
print(np.sum(array,axis=1)) #sum of Rows
