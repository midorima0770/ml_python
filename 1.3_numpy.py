import numpy as np

"""

    https://pycode.ru/numpy_tasks.html
    
"""

#1
print(np.version.version)

print()

#2
arr_2 = np.array([i for i in range(10)])
print(arr_2)

print()

#3
arr_3 = np.ones((3,3),bool)
print(arr_3)

print()

#4
arr_4 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr_4 = arr_4[arr_4 % 2 == 1]
print(arr_4)

print()

#5
arr_4 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr_4[arr_4 % 2 == 1] = -1
print(arr_4)

print()

#6
arr_4 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr_res_4 = np.array([(i if i%2==0 else -1) for i in arr_4])
print(arr_res_4)
print(arr_4)

print()

#7
n_7 = 10
arr_7 = np.arange(n_7)
arr_7 = arr_7.reshape(2,int(n_7/2))
print(arr_7)

print()

#8
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
c = np.vstack((a, b))
print(c)

print()

#9
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
c = np.hstack((a, b))
print(c)

print()

#11
a_11 = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b_11 = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
result_11 = np.intersect1d(a_11,b_11)
print(result_11)

print()

#12
a_12 = np.array([1, 2, 3, 4, 5])
b_12 = np.array([5, 6, 7, 8, 9])
a_12 = a_12[np.isin(a_12,b_12,invert=True)]
print(a_12)

print()

#13
a_13 = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b_13 = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
indices = np.where(np.isin(a_13, b_13))
print(indices)

print()

#14
a_14 = np.array([2, 6, 1, 9, 10, 3, 27])
a_14 = a_14[(a_14 > 5) & (a_14 <= 10)]
print(a_14)

print()

#16
arr_16 = np.arange(9).reshape(3, 3)
arr_16[:, [0, 1]] = arr_16[:, [1, 0]]
print(arr_16)

print()

#17
arr_17 = np.arange(9).reshape(3, 3)
arr_17[[0, 1],:] = arr_17[[1,0],:]
print(arr_17)

print()

#18
arr_18 = np.arange(9).reshape(3, 3)
arr_18[[0,-1], :] = arr_18[[-1,0], :]
print(arr_18)

print()

#19
arr_19 = np.arange(9).reshape(3, 3)
arr_19[:,[0,-1]] = arr_19[:,[-1,0],]
print(arr_19)

print()

#20
arr_20 = np.random.random((5, 3))
arr_20 = 5 + arr_20 * (10 - 5)
print(arr_20)


"""

    https://www.kaggle.com/code/sokolovaleks/100-numpy-exercises-rus-version

"""

#3
z_3 = np.zeros(10)
print(z_3)

print()

#4
Z = np.zeros((10,10))
print('Исходный вектор Z: \n', Z)
print("Размер памяти занимаемый вектором Z: %d байт" % (Z.size * Z.itemsize))

print()

#5
print(np.info(np.add))

print()

#6
z_6 = np.ones(10,int)
print(z_6)

print()

#7
z_7 = np.arange(10,50)
print(z_7)

print()

#8
z_8 = np.arange(50)
z_8 = z_8[::-1]
print(z_8)

print()

#9
z_9 = np.arange(9).reshape(3, 3)
print(z_9)

print()

#10
z_10 = np.array([1,2,0,0,4,0])
print(z_10.nonzero())

print()

#11
z_11 = np.ones(9,int).reshape((3,3))
print(z_11)

print()

#12
z_12 = np.random.randint(low=0 , high= 3,size=(3,3,3))
print(z_12)

print()

#13
z_13 = np.random.randint(low=0, high= 10,size=(10,10))
print(z_13.min(),z_13.max())

print()

#14
z_14 = np.random.randint(low=1,high=100,size=30)
print(z_14.mean())

print()

#15
z_15 = np.zeros((5,10))
z_15[:,0],z_15[:,9] = 1,1
z_15[0,:],z_15[4,:]=1,1
print(z_15)

print()

#16
z_16 = np.ones((5,5),int)
z_16 = np.pad(z_16,pad_width=1)
print(z_16)

print()

#18
a_18 = 1+np.arange(4)
z_18 = np.diag(a_18,k=-1)
print(z_18)

#19
z_19 = np.zeros((8,8))
z_19[::2,::2] = 1
print(z_19)

#20
