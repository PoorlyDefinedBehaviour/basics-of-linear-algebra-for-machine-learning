import numpy

a1 = numpy.array([1, 2, 3])
# [1 2 3]
print(a1)

a2 = numpy.array([4, 5, 6])
# [4 5 6]
print(a2)

a3 = numpy.hstack((a1, a2))
# [1 2 3 4 5 6]
print(a3)

# (6,)
print(a3.shape)
