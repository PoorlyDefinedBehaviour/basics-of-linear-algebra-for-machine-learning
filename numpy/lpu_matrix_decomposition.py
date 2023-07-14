import numpy
import scipy

a = numpy.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
print(a)

p, l, u = scipy.linalg.lu(a)

# [[0. 1. 0.]
#  [0. 0. 1.]
#  [1. 0. 0.]]
print(p)

# [[1.         0.         0.        ]
#  [0.14285714 1.         0.        ]
#  [0.57142857 0.5        1.        ]]
print(l)

# [[7.         8.         9.        ]
#  [0.         0.85714286 1.71428571]
#  [0.         0.         0.        ]]
print(u)

# Reconstruct the matrix from its components.
#
# [[1. 2. 3.]
#  [4. 5. 6.]
#  [7. 8. 9.]]
print(p.dot(l).dot(u))
