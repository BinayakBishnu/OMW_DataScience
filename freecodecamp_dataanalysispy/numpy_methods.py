import numpy as np

a = np.array([[3, 4, 1],
              [9, 2, 4],
              [3, 7, 2], ])


print(np.linalg.eig(a))
print(np.linalg.det(a))

b = np.array([[2, 5, 1],
     [6, 2, 5], ])
c = np.array([[3, 6],
     [6, 2],
     [2, 6],
     [7, 9], ])

# print(b*c)
# print(c*b)

# print(np.matmul(b, c))
print(np.matmul(c, b))

a = np.array([[3, 5, 1, 7, 9, 4, ],
     [5, 2, 5, 1, 2, 3, ],
     [8, 5, 4, 7, 0, 1, ]])
print(a)
b = a.reshape((9, 2))
print(b)

m = np.arange(10)
print(m)
print(m+10)
