import numpy as np

ages = np.array([[21,17,19,20,16,30,18,65],
                [39,22,15,99,18,19,20,21]])
teenagers = ages[ages<=19]
print(teenagers) #2D array gets flattened (boolean indexing takes place)

adults = ages[(ages>=18) & (ages<=65)] # & is used bcoz numpy uses C-programming styled arrays
print(adults)

seniors = ages[ages>65]
print(seniors)

evens = ages[ages%2==0]
print(evens)

seniors = np.where(ages>=65,ages,0)
print(seniors)
