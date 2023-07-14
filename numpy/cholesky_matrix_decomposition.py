import numpy

a = numpy.array([
    [2, 1, 1],
    [1, 2, 1],
    [1, 1, 2]
])

l = numpy.linalg.cholesky(a)

# [[1.41421356 0.         0.        ]
#  [0.70710678 1.22474487 0.        ]
#  [0.70710678 0.40824829 1.15470054]]
print(l)

# Reconstruct the matrix.
#
# [[2. 1. 1.]
#  [1. 2. 1.]
#  [1. 1. 2.]]
print(l.dot(l.T))
