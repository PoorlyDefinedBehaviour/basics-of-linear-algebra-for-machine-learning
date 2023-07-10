import numpy

data = numpy.array([
    [11, 22, 33],
    [44, 55, 66],
    [77, 88, 99]
])

split = 2

training_data, testing_data = data[:split], data[split:]

# [
#   [11, 22, 33],
#   [44, 55, 66],
# ]
print(training_data)

# [
#   [77, 88, 99]
# ]
print(testing_data)
