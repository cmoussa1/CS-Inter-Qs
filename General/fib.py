# Write fibonaci sequence iteratively and recursively

import time

# Recursive Solution (O(n^2) solution time)
def F_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F_recursive(n - 1) + F_recursive(n - 2)

start = time.time()
print F_recursive(35)
end = time.time()
print "Total computation time: " + str(end - start) + " seconds"

# Iterative Solution
def F_iterative(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    elif (n > 1):
        fn = 0
        fn1 = 1
        fn2 = 2
        for i in range(3, n):
            fn = fn1+fn2
            fn1 = fn2
            fn2 = fn
        return fn
    else:
        return -1

start = time.time()
print F_iterative(35)
end = time.time()
print "Total computation time: " + str(end - start) + " seconds"

# Recursive Memoization Solution
memo = {}
def F_memoize(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    elif (n > 1):
        if n not in memo:
            memo[n] = (F_memoize(n - 1) + F_memoize(n - 2))

        return memo[n]
    else:
        return -1

start = time.time()
print F_memoize(35)
end = time.time()
print "Total computation time: " + str(end - start) + " seconds"


"""
Explanation:

    Pretty straightforward solution. Difference between recursive and iterative
    methods is that F(0) and F(1) are hardwired cases, and for each successive
    value, iteratively add the values for larger values of n. Recursive methods
    involve breaking down the problem into successively smaller problems and
    then working back out, which results in long computation time (O(n^2)).
    However, if we memoize the recursive method (save previously computed
    answers, we can now compute larger Fibonacci numbers much more quickly).
"""
