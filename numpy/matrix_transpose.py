import numpy

# A matrix can be transposed, which creates a new matrix with
# the number of columns and rows flipped.
#
# C = A{superscript T}

a = numpy.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

# [[1 2]
#  [3 4]
#  [5 6]]
print(a)

# [[1 3 5]
#  [2 4 6]]
print(a.T)
