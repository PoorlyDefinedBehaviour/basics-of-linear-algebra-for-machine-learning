import numpy

data = numpy.array([
    [11, 22],
    [33, 44],
    [55, 66]
])

# 11
print(data[0, 0])

# 11
print(data[0][0])

# Get all elements in the first row.
# [11 22]
print(data[0, ])
