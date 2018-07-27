# Implement a binary search of a sorted array of integers

def binary_search(arr, value):

    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2
        if value > arr[mid]:
            left = mid + 1
        else:
            right = mid
    if left != len(arr) and arr[left] == value:
        return "At index " + str(left)
    else:
        raise ValueError("{!r} is not in sequence".format(value))

print binary_search([1,2,3,4,5,6,7,14,56,87,99], 14)


"""
Explanation:

    Uses the Binary Search Tree algorithm to search for a specific value in
    a sorted array. Looks at the middle element in the list. If it is greater,
    then it divides the greater half of the list in half and searches again
    for the middle element until it finds the element; otherwise, return that
    it isn't found.
"""
