import numpy

# A trace of a square matrix is the sum of the values on the main diagonal.
#
# tr(A)

a = numpy.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
print(a)

# 15
print(numpy.trace(a))
