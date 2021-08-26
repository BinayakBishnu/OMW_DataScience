import numpy as np

""" a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.dot(a, b)) """

""" A = np.array([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            ])

b = np.array([10, 20, 30])

print(A@b) """


""" import t urllib.request
urllib.request.urlretrieve(
    'https://hub.jovian.ml/wp-content/uploads/2020/08/climate.csv', 
    'climate.txt')

data = np.genfromtxt('climate.txt',delimiter=',',skip_header=1)

print(data)

print(data.shape) """

arr2 = np.array([[1, 2, 3, 4], 
                [5, 6, 7, 8], 
                [9, 1, 2, 3]])
arr3 = np.array([[11, 12, 13, 14], 
                [15, 16, 17, 18], 
                [19, 11, 12, 13]])

print(arr2)
xyz = arr2 + 3
print(xyz)
abc = arr3-arr2
print(abc)
abc2 = arr2/2
print(abc2)
arr2*arr3 # element-wise multiplication


