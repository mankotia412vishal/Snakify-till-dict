"""Given two lists of numbers. Count how many unique numbers occur in both of them.
This task can be solved in one line of code.
"""
print(len(set(input().split()) & set(input().split())))
