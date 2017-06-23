import math

Sum = 0
for i in range(12):
    P = (100) * math.sin(math.pi * (i/12.0))
    Sum += P
    print "{} Sum: {}, actual: {}".format(i, P, Sum)
