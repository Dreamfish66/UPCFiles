import numpy as np

#array
array1 = np.array([1,2,3])
print(array1)

array2 = np.zeros(10)
print(array2)
array2 = np.ones(10)
print(array2)
array2 = np.random.random(10)
print(array2)

array3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
array4 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array3 + array4)
print(array3 * array4)
print(array3 - array4)
print(array3 / array4)
#calculate directly

print(array3[0])
print(array3[0][0])
print(array3[0,2])
print(array3[0:2])
print(array3[0:2,0:2])
print(array3.max())
print(array3.min())
print(array3.sum())


#matrix
matrix1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix1)
print(np.ones((3,2)))
print(np.zeros((2,3)))

data = np.array([1,2,3])
powers_of_ten = np.array([[1,10],[100,1000],[10000,100000]])
print(data.dot(powers_of_ten))#dot product

print(np.random.random((2,3)).T)#transpose

oneMatrix = np.array([1,2,3,4,5,6,7,8,9])
twoMatrix = oneMatrix.reshape((3,3))
print(twoMatrix)