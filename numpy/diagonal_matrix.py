import numpy

matrix = numpy.array([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
])


# Create a diagonal matrix from `matrix`.
vector = numpy.diag(matrix)

# [1 2 3]
print(vector)

# Create a diagonal matrix from a vector representing a diagonal matrix.
#
# [[1 0 0]
#  [0 2 0]
#  [0 0 3]]
print(numpy.diag(vector))
