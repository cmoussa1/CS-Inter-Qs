# Given 2 integer arrays, determine if the 2nd array is a rotated version of
# the 1st array.
# ex. original array A = {1,2,3,4,6,7,8}
#     rotated  array B = {5,6,7,8,1,2,3}

def check_if_rotated(u, v):
    n, i, j = len(u), 0, 0
    if n != len(v):
        return False
    while i < n and j < n:
        k = 1
        while k <= n and u[(i + k) % n] == v[(j + k) % n]:
            k += 1
        if k > n:
            return True
        if u[(i + k) % n] > v[(j + k) % n]:
            i += k
        else:
            j += k
    return False

print check_if_rotated([3,1,2,3,4], [3,4,3,1,2])
print check_if_rotated([3,1,2,3,4], [3,4,3,2,1])

"""
The Explanation:

    This finds maximal suffixes of u and v and checks if they are identical
    on prefixes of size n.
"""
