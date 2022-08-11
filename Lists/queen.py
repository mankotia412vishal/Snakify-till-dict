# In chess it is known that it is possible to place 8 queens on an 8×8 chess
#  board such that none of them can attack another. Given a placement of 8 
#  queens on the board, determine if there is a pair of queens that can attach 
#  each other on the next move. Print the word NO if no queen can attack another,
#   otherwise print YES. The input consists of eight coordinate pairs, one pair per line, 
#   with each pair
#  giving the position of a queen on a standard chess board with rows and 
#  columns numbered starting at 1.

N = 8
result = 'NO'
x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = [int(j) for j in input().split()]
for i in range(N):
    for j in range(i+1, N):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            result = 'YES'
print(result)
