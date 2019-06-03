from sympy import *
import numpy as np


# This process is using Symbolic Differentiation
# take derivative with respect to this variable
x = Symbol('x')
# Function
y = x**2 + 1

# derivative
y_prime = y.diff(x)
print(y_prime)
