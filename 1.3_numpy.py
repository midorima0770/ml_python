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

#13
a_13 = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b_13 = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])