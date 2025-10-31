import numpy as np

# print(np.__version__)

my_list = [1,2,3,4]
# my_list = my_list *2
# # print(my_list)

my_list_np = np.array(my_list) #array is a function here
my_list_np *= 2
print(my_list_np)
print(type(my_list_np))

print(my_list_np.ndim) #gives the dimension of the array ie 1 in this case.

array = np.array('A')
print(array.ndim) #0D
print(array.shape)

array_1 = np.array(['A','B','C']) #1D
print(array_1.shape)

array_2 = np.array([['A','B','C'],
                    ['D','E','F'],
                    ['G','H','I']]) #2D
print(array_2.shape)

array_3 = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                   [['J','K','L'],['M','N','O'],['P','Q','R']],
                   [['S','T','U'],['V','W','X'],['Y','Z',' ']]]) #3D
print(array_3.shape)

#Chain Indexing
print(array_1[0]) #A
print(array_2[1][0]) #D
print(array_3[2][0][0]) #S

#Multidimensional Indexing (Better than Chain Indexing)
print(array_1[1]) #B
print(array_2[1,0]) #D
print(array_3[2,0,0]) #S

#Writing a Word from our Array
word = array_3[0,0,2] + array_3[0,0,0] + array_3[2,0,1]
print(word) #prints CAT
