import numpy
import math

a = numpy.array([1, 2, 3])

# The L^1 norm is the sum of the absolute values of a vector.
# 6.0
print(numpy.linalg.norm(a, 1))

# The L^2 norm is the sqrt of sum of the elements of the vector squared.
# 3.7416573867739413
print(numpy.linalg.norm(a))

# The vector max norm (L^inf) is the maximum value of the vector.
# 3.0
print(numpy.linalg.norm(a, math.inf))
