# Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce

def max_list(a, b):
    return a if a>=b else b

nums = [2, 6, 8, 1, 5]
max_num = reduce(max_list, nums)
print(max_num)