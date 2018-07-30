# Implement the square root function

# Using a built-in Python library...
from math import sqrt

def square_root(n):
    return sqrt(n)

print square_root(1)
print square_root(4)
print square_root(9)
print square_root(16)

# Our own implementation...
# Uses Babylonian method
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots
def own_square_root(n):
    error_margin = 1
    if n < 0:
        return None
    a = 1
    b = n
    while (abs(a - b) > error_margin):
        a = (a + b) / 2
        b = n / a
    return a

print own_square_root(1)
print own_square_root(4)
print own_square_root(9)
print own_square_root(16)
