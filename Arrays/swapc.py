"""Given two positive integers m and n, m lines of n elements, giving an m×n matrix A, followed by two non-negative integers i and j less than n, swap columns i and j of A and print the result.
Write a function swap_columns(a, i, j) and call it to exchange the columns.
"""


def swap_columns(a, i, j):
    for row in a:
        row[i], row[j] = row[j], row[i]
    return a


n, m = [int(k) for k in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(k) for k in input().split()]
for row in swap_columns(a, i, j):
    print(' '.join([str(i) for i in row]))
