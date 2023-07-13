import numpy

# rank(A)

# 1
print(numpy.linalg.matrix_rank(numpy.array([1, 2, 3])))

# 0
print(numpy.linalg.matrix_rank(numpy.array([0, 0, 0, 0, 0])))

# 0
print(numpy.linalg.matrix_rank(numpy.array([
    [0, 0],
    [0, 0]
])))

# 1
print(numpy.linalg.matrix_rank(numpy.array([
    [1, 2],
    [1, 2]
])))

# 2
print(numpy.linalg.matrix_rank(numpy.array([
    [1, 2],
    [3, 4],
])))
