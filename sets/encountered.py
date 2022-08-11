"""""Given a sequence of numbers, determine if the next number has already been encountered. For each number, print the word YES (in a separate line) if this number has already been encountered, and print NO, if it has not already been encountered."""""


a = input().split()
for i in range(len(a)):
    if a[i] in a[:i]:
        print('YES')
    else:
        print('NO')
