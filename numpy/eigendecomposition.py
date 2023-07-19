import numpy

a = numpy.array([
    [1, 2, 3],
    [3, 4, 5],
    [7, 8, 9]
])

eigen_values, eigen_vectors = numpy.linalg.eig(a)

# [ 1.51853528e+01 -1.18535277e+00  8.01676920e-16]
print(eigen_values)

# [[ 0.24504916  0.69993888  0.40824829]
#  [ 0.44967306  0.24272908 -0.81649658]
#  [ 0.85892086 -0.67169052  0.40824829]]
print(eigen_vectors)

# [ 3.72115787  6.82844402 13.04301634]
print(a.dot(eigen_vectors[:, 0]))

# [ 3.72115787  6.82844402 13.04301634]
print(eigen_vectors[:, 0] * eigen_values[0])
