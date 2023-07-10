import numpy

data = numpy.array([11, 22, 33, 44, 55])

# (5, ) 5 columns
print(data.shape)

data = numpy.array([
    [11, 22],
    [33, 44],
    [55, 66]
])

# (3, 2) 3 rows and 2 columns
print(data.shape)
