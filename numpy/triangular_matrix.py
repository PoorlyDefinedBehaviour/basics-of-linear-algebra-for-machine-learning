import numpy

matrix = numpy.array([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
])

# [[1 0 0]
#  [1 2 0]
#  [1 2 3]]
print(numpy.tril(matrix))

# [[1 2 3]
#  [0 2 3]
#  [0 0 3]]
print(numpy.triu(matrix))
