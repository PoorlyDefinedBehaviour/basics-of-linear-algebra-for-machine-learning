import numpy
import scipy

a = numpy.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

u, s, v = scipy.linalg.svd(a)

# [[-0.2298477   0.88346102  0.40824829]
#  [-0.52474482  0.24078249 -0.81649658]
#  [-0.81964194 -0.40189603  0.40824829]]
print(u)

# [9.52551809 0.51430058]
print(s)

# [[-0.61962948 -0.78489445]
#  [-0.78489445  0.61962948]]
print(v)
