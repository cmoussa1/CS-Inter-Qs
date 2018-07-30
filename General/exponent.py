# Implement an exponent function

# Using a built-in Python library...
from math import pow

def exponent(x, n):
    return pow(x, n)

print exponent(1, 2)
print exponent(2, 2)
print exponent(3, 2)
print exponent(4, 2)

# Our own implementation O(n)
def own_exponent(x, n):
    if (n == 0):
        return 1
    elif (int(n % 2) == 0):
        return (own_exponent(x, int(n / 2)) * own_exponent(x, int(n / 2)))
    else:
        return (x * own_exponent(x, int(n / 2)) * own_exponent(x, int(n / 2)))

# Driver Code
print own_exponent(1, 2)
print own_exponent(2, 2)
print own_exponent(3, 2)
print own_exponent(4, 2)

# Optimized solution O(log(n))
# stores own_exponent_2(x, y/2) only once and stores it
def own_exponent_2(x, y):

    if(y == 0): return 1
    temp = own_exponent_2(x, int(y / 2))

    if (y % 2 == 0):
        return temp * temp
    else:
        if(y > 0): return x * temp * temp
        else: return (temp * temp) / x

print own_exponent_2(1, 2)
print own_exponent_2(2, 2)
print own_exponent_2(3, 2)
print own_exponent_2(4, 2)
