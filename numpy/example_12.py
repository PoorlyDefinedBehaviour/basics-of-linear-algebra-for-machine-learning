import numpy

data = numpy.array([
    [11, 22, 33],
    [44, 55, 66],
    [77, 88, 99]
])

# X = all rows and columns except last one.
# y = last column of every row.
X, y = data[:, : -1], data[:, -1]
print(X)
print(y)
