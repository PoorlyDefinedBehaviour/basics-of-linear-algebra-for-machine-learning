import numpy

# The determinant is the product of all the eigenvalues of the matrix.
#
# A determinant of 1 preserves the space of the matrix matrix when it is multiplied
# with the matrix in question.
#
# The determinant is zero when the matrix has no inverse.
#
# det(A) or |A|

a = numpy.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# 0.0
print(numpy.linalg.det(a))
