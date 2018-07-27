# Find the most frequent integer in an array

from collections import Counter

def most_common(lst):
    data = Counter(lst)
    return max(lst, key=data.get)


# will return 1
print most_common([1,2,3,4,5,1,3,4,5,1,6,7,1,8,9,1,10])

"""
The Explanation:

    max returns the largest item in an iterable or the largest of two or more
    arguments. The key argument specifies a one-argument ordering function;
    if supplied, it must be in keyword form.

    Counter is a dict subclass used for counting hashable objects. It's an
    unordered collection where elements are stored as dict keys and counts
    are stored as dict values.

    In our example, we are returning the max of a list of integers and the
    ordering function data.get is simply fetching each element in the list,
    thus giving an algorithm time of O(n).
"""
