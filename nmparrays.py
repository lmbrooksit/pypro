from traceback import print_tb

import numpy as np
import matplotlib.pyplot as plt

mylist = [1,2,3]
print(mylist)
print(type(mylist))

print(np.array(mylist))

myarray = np.array(mylist)
print(myarray)

print(type(myarray))

print(np.arange(0,10))

print(np.arange(0,10,2))

print(np.zeros(shape=(5,5)))
print(np.zeros(shape=(10,5)))

print(np.ones(shape=(2,4)))

print(np.sqrt(400000000000000))

np.random.seed(101)
arr = np.random.randint(0,100,10)
print(arr)

arr2 = np.random.randint(0,100,10)
print(arr2)

print(arr.max())
print(arr.argmax())

print(arr.min())

print(arr.argmin())

print(arr.mean())

print(arr.reshape((5,2)))

mat = np.arange(0,100).reshape(10,10)

print(mat.shape)
print(mat)

row = 4
col = 6

print(mat[row,col])

print(mat[:,1])
print(mat[:,1].shape)
print(mat[:,1].reshape(10,1))

print(mat[2,:])

print(mat[0:3,0:4])

mat[0:3,0:4] = 0

mynewmat = mat.copy()

print(mynewmat)

mynewmat[0:6,:] = 999
mynewmat2 = mynewmat.copy()
print(mynewmat2)