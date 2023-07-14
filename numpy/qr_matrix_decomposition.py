import numpy

a = numpy.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

q, r = numpy.linalg.qr(a)

# [[-0.16903085  0.89708523]
#  [-0.50709255  0.27602622]
#  [-0.84515425 -0.34503278]]
print(q)

# [[-5.91607978 -7.43735744]
#  [ 0.          0.82807867]]
print(r)

# Reconstruct the matrix.
#
# [[1. 2.]
#  [3. 4.]
#  [5. 6.]]
print(q.dot(r))
