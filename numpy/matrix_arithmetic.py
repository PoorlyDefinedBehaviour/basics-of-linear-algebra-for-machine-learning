import numpy

# Matrix addition
# c[i][j] = a[i][j] + b[i][j]

a = numpy.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = numpy.array([
    [1, 2, 3],
    [4, 5, 6]
])

# [[ 2  4  6]
#  [ 8 10 12]]
print(a+b)

# Matrix subtraction
# c[i][j] = a[i][j] - b[i][j]

# [[0 0 0]
#  [0 0 0]]
print(a-b)


# Matrix multiplication (Hadamard product) (A o B)
# c[i][j] = a[i][j] * b[i][j]

# [[ 1  4  9]
#  [16 25 36]]
print(a*b)


#  Matrix division
# c[i][j] = a[i][j] / b[i][j]

# [[1. 1. 1.]
#  [1. 1. 1.]]
print(a/b)

# Matrix-Matrix multiplication (also called the matrix dot product) (A. B)
# C(m, k) = A(m, n) . B(n, k)
# requires:
#   columns(A) == rows(B)

a = numpy.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

b = numpy.array([
    [1, 2],
    [3, 4]
])

# [[ 7 10]
#  [15 22]
#  [23 34]]
print(a.dot(b))

# [[ 7 10]
#  [15 22]
#  [23 34]]
print(a @ b)  # sam as a.dot(b) ?

# Matrix-vector multiplication
# Multiply each column with the vector element at the column number.
# requires:
#   columns(matrix) == len(vector)

a = numpy.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

b = numpy.array([0.5, 0.5])

# [1.5 3.5 5.5]
print(a.dot(b))

# Matrix-scalar multiplication
# c[i][j] = a[i][[j] * scalar

a = numpy.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

# [[0.5 1. ]
#  [1.5 2. ]
#  [2.5 3. ]]
print(a * 0.5)
