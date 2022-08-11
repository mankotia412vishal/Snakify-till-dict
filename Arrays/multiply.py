"""Given three positive integers m, n and r, m lines of n elements, giving an m×n matrix A, and n lines of r elements, giving an n×r matrix B, form the product matrix AB, which is the m×r matrix whose(i, k) entry is the sum
A[i][1]∗B[1][k] +⋯+A[i][n]∗B[n][k]
and print the result.
"""

m, n, r = [int(k) for k in input().split()]
A = [[int(k) for k in input().split()] for i in range(m)]
B = [[int(k) for k in input().split()] for j in range(n)]
C = [[0]*r for i in range(m)]

for i in range(m):
    for k in range(r):
        for j in range(n):
            C[i][k] += A[i][j] * B[j][k]

print('\n'.join([' '.join([str(k) for k in row]) for row in C]))
