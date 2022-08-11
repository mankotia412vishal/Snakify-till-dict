# You are given a dictionary consisting of word pairs. Every word is a synonym the other word in its pair. All the words in the dictionary are different.
# After the dictionary there's one more word given. Find a synonym for him.


n = int(input())
d = {}
for i in range(n):
    first, second = input().split()
    d[first] = second
    d[second] = first
print(d[input()])
