import numpy

data = numpy.array([11, 22, 33, 44, 55])

# (5,)
print(data.shape)

data = data.reshape((data.shape[0], 1))
# (5, 1)
print(data.shape)
