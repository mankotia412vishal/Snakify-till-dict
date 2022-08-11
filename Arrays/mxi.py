"""Given two integers representing the rows and columns(m×n), and subsequent m rows of n elements, find the index position of the maximum element and print two numbers representing the index(i×j) or the row number and the column number. If there exist multiple such elements in different rows, print the one with smaller row number. If there multiple such elements occur on the same row, output the smallest column number.

"""

n, m = [int(j) for j in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
max_row = 0
max_col = 0
max = a[max_row][max_col]
for i in range(n):
    for j in range(m):
        if max < a[i][j]:
            max = a[i][j]
            max_row = i
            max_col = j
print(max_row, max_col)
