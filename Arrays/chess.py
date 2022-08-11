"""Given two numbers n and m. Create a two-dimensional array of size(n×m) and populate it with the characters "." and "*" in a checkerboard pattern. The top left corner should have the character "." .
"""


def chessboard(n, m):
    if (n + m) % 2 == 0:
        return '.'
    else:
        return '*'


n, m = [int(j) for j in input().split()]
a = [[chessboard(i, j) for j in range(m)] for i in range(n)]
for row in a:
    print(' '.join(row))
