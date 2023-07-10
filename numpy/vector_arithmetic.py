import numpy

# Two vectors of equal length can be added together to create a new vector.

a = numpy.array([1, 2, 3])
b = numpy.array([1, 2, 3])

# [2, 4, 6]
print(a+b)

# [0 0 0]
print(a-b)

# [1 4 9]
print(a * b)

# [1.0 1.0 1.0]
print(a/b)

# 14
print(a.dot(b))

# [0.5, 1.0, 1.5]
print(a * 0.5)
