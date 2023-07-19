import numpy

m = numpy.array([
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6]
])

# column means
#
# [1. 2. 3. 4. 5. 6.]
print(numpy.mean(m, axis=0))

# row means
#
# [3.5 3.5]
print(numpy.mean(m, axis=1))
