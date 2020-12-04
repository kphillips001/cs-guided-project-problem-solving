"""
Challenge #3:

Given a string of numbers separated by a comma and space, return the product of the numbers.

Examples:
- multiply_nums("2, 3") ➞ 6
- multiply_nums("1, 2, 3, 4") ➞ 24
- multiply_nums("54, 75, 453, 0") ➞ 0
- multiply_nums("10, -2") ➞ -20

Notes:
- Bonus: Try to complete this challenge in one line!
"""

# Product => multiply
# Understand the given string
# Multiply all numbers inside of string
# Edge cases => decimals - no => one number? empty string?

# Plan
# Convert input into numbers => maybe array
# Can use split method => use .split(", ")

def multiply_nums(nums):
    # Your code here
    # Use for over all nums => turn into int => multiply info final
    nums_array = nums.split(', ')
    final_val = 1
    for num in nums_array:
        final_val *= int(num)
    return final_val

print(multiply_nums("54, 75, 453, 0"))
print(multiply_nums("2, 3"))
print(multiply_nums("1, 2, 3, 4"))
print(multiply_nums("10, -2"))