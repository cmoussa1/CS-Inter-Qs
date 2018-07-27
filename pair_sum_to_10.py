# Find pairs in an integer array whose sum is equal to 10
#   Bonus: do it in linear time

import sys

def pairs_sum_to_10(arr, n, sum):

    m = [0] * 1000

    # Store counts of all elements in map m
    for i in range(0, n):
        m[arr[i]]
        m[arr[i]] += 1

    twice_count = 0

    # Iterate through each element and increment
    # the count (Notice that every pair is
    # counted twice)
    for i in range(0, n):

        twice_count += m[sum - arr[i]]

        # if (arr[i], arr[i]) pair satisfies the
        # condition, then we need to ensure that
        # the count is decreased by one such
        # that the (arr[i], arr[i]) pair is not
        # considered
        if (sum - arr[i] == arr[i]):
            twice_count -= 1

    # return the half of twice count
    return int(twice_count / 2)

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = len(arr)
    sum = 10

    print("Count of pairs is", pairs_sum_to_10(arr, n, sum))

main()

"""
The Explanation:

    This creates a map to store frequency of each number in the array (in a
    single traversal). In the next traversal, for each element check if it can
    be combined with any other element (other than itself) to give the desired
    sum. Increment the counter accordingly. After completion of second
    traversal, we'd have twice the required value stored in counter because
    every pair is counted two times. Hence divide the count by 2 and return.
"""
