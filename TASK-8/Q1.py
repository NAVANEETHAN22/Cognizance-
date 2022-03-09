str = input("Q1) To build a new vector with 5 consecutive zeros interleaved between each value")
import numpy as np
a = np.array([10,11,12,13,14])
na = 5
a0 = np.zeros(len(a) + (len(a)-1)*(na))
a0[::na+1] = a
print(a0)
