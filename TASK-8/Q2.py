str = input("Q2) TO CHECK THE ARRAYS ARE EQUAL")
import numpy as np
a = np.random.randint(0,2,6)
print("FIRST ARRAY:")
print(a)
b = np.random.randint(0,2,6)
print("SECOND ARRAY:")
print(b)
array_equal = np.allclose(a, b)
print(array_equal)
