# Find the common elements of 2 int arrays

def find_commons(lst1, lst2):

    return list(set(lst1).intersection(lst2))

print find_commons([1,2,3,4,5], [3,4,5,6,7,8,9,10])


"""
Explanation:

    Here we can just use basic logic functionality between two lists to find
    the commond elements.
"""
