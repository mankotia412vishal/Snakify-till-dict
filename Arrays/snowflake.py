"""Given an odd number integer n, produce a two-dimensional array of size(n×n). Fill each element with a single character string of "." . Then fill the middle row, the middle column and the diagnals with the single character string of "*" (an image of a snow flake). Print the array elements in (n×n) rows and columns and separate the characters with a single space.
"""

n = int(input())
k = n // 2
a = [['.'] * n for i in range(n)]
for i in range(n):
    a[k][i] = '*'
    a[i][k] = '*'
    a[i][i] = '*'
    a[n-i-1][i] = '*'
for row in a:
    print(' '.join(row))
