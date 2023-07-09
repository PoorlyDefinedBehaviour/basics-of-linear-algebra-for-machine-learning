import numpy

a1 = numpy.array([1, 2, 3])
# [1 2 3]
print(a1)

a2 = numpy.array([4, 5, 6])
# [4 5 6]
print(a2)

# vstack stands for vertical stack because the arrays are put "on top" of each other.
# Each array becomes a row.
a3 = numpy.vstack((a1, a2))
# [
#   [1 2 3],
#   [4 5 6]
# ]
print(a3)

# (2, 3)
print(a3.shape)
