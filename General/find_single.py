# Find the only element in an array that only occurs once

def find_single(arr, n):

    res = arr[0]

    # Do XOR of all elements and return
    for i in range(1, n):
        res = res ^ arr[i]

    return res

arr = [2, 3, 5, 4, 5, 3, 4]
print "Element occuring once is", find_single(arr, len(arr))


"""
Explanation:

    The best solution is to use XOR of all array elements, which gives us the
    number with a single occurrence. The idea is based on the following
    two facts:

        a) XOR of a number with itself is 0.
        b) XOR of a number with 0 is the number itself.
"""
