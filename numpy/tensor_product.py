import numpy

a = numpy.array([1, 2])

b = numpy.array([3, 4])

# [[3 4]
#  [6 8]]
print(numpy.tensordot(a, b, axes=0))
