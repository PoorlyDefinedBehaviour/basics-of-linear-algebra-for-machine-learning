import numpy

a = numpy.array([
    [1, 2, 3],
    [1, 2, 3]
])

print(a.shape)

b = numpy.array([1, 2])

print(b.shape)

c = a + b

# ValueError: operands could not be broadcast together with shapes (2,3) (2,)
print(c)
