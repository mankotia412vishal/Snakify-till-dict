"""Given an integer n, create a two-dimensional array of size(n×n) and populate it as follows, with spaces between each character:
The positions on the minor diagonal(from the upper right to the lower left corner) receive 1 .
The positions above this diagonal recieve 0 .
The positions below the diagonal receive 2 .
Print the elements of the resulting array.
"""

n = int(input())
a = [0] * n
a = [[0] * (n - i - 1) + [1] + [2] * i for i in range(n)]
for row in a:
    print(' '.join([str(i) for i in row]))
