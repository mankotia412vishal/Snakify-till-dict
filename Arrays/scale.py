"""Given two positive integers m and n, m lines of n elements, giving an m×n matrix A, followed by one integer c, multiply every entry of the matrix by c and print the result.
"""

m, n = [int(k) for k in input().split()]
a = [[int(k) for k in input().split()] for i in range(m)]
c = int(input())

for i in range(m):
    for j in range(n):
        a[i][j] *= c
print('\n'.join([" ".join([str(k) for k in row]) for row in a]))
