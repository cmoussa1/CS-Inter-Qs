# Prints out the binary form of an integer

def conv_to_bin(num):
    return bin(num)

print conv_to_bin(1)
print conv_to_bin(2)
print conv_to_bin(3)
print conv_to_bin(4)

def int_to_bin_string(i):
    if i == 0:
        return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i //= 2
    return s

print int_to_bin_string(1)
print int_to_bin_string(2)
print int_to_bin_string(3)
print int_to_bin_string(4)

"""
Explanation:

    Python has a built-in bin() method that you can call to convert from int to
    its binary representation.

    However, if we're not allowed to use that method, we can write our own
    method. Take the input string and use logic operations to convert the
    digits into its binary representation. 
"""
