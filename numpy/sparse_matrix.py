import numpy
import scipy

a = numpy.array([
    [1, 0, 0, 1, 0, 0],
    [0, 0, 2, 0, 0, 1],
    [0, 0, 0, 2, 0, 0]
])

s = scipy.sparse.csr_matrix(a)

# (0, 0)        1
# (0, 3)        1
# (1, 2)        2
# (1, 5)        1
# (2, 3)        2
print(s)

# [[1 0 0 1 0 0]
#  [0 0 2 0 0 1]
#  [0 0 0 2 0 0]]
print(s.todense())

# 0.7222222222222222
print(1.0 - numpy.count_nonzero(a) / a.size)
