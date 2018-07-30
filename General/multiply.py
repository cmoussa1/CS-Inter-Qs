# Multiply function that multiplies 2 integers without using *

def multiply(x ,y):
    product = 0
    for i in range(0, y):
        product += x
    return product

print multiply (1,1)
print multiply (2,2)
print multiply (3,3)
print multiply (4,4)


"""
Explanation:

Instead of multiplying x and y, we can just add x for y times
"""
