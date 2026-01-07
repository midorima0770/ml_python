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

