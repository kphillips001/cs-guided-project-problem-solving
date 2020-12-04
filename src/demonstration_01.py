"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
"""
# inputs/outputs
# list of nums
# number of items from end of list
# outputs - list or invalid
# edge cases - invalid if n > len of list = [] if n = 0

# Plan
# Pseudo Code
# Plain English
# How do we handle edge cases
# How to handle main problem => get last n elements of list
# [ : ] or slice => get all elements starting length - n


def last(arr, n):
    # Your code here
    # Edge cases
    if n > len(arr):
        return 'invalid'
    elif n == 0:
        return []
    # main solution
    return arr[len(arr) - n : ] # Returns a subarray n: => represents end of array
    # : => indicates the end of an array

print(last([1, 2, 3, 4, 5], 1))
print(last([4, 3, 9, 9, 7, 6], 3))
print(last([1, 2, 3, 4, 5], 7) )
print(last([1, 2, 3, 4, 5], 0))