import numpy

data = [
    [11, 22],
    [33, 44],
    [55, 66]
]

data = numpy.array(data)

# (3, 2)
print(data.shape)

data = data.reshape((data.shape[0], data.shape[1], 1))

# (3, 2, 1)
print(data.shape)
