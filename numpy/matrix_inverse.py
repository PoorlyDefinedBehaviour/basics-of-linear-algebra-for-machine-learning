import numpy

# Matrix inversion is finding another matrix that when multiplied with the matrix,
# results in an identity matrix.
#
# Operation: A{superscript -1}

a = numpy.array([
    [1.0, 2.0],
    [3.0, 4.0]
])

# [[1. 2.]
#  [3. 4.]]
print(a)

b = numpy.linalg.inv(a)

# [[-2.   1. ]
#  [ 1.5 -0.5]]
print(b)

# [[1.0000000e+00 0.0000000e+00]
#  [8.8817842e-16 1.0000000e+00]]
print(a.dot(b))
