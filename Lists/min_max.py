# Given a list of unique numbers, swap the minimal and maximal elements of this list. Print the resulting list.
# 
a = [int(s) for s in input().split()]
m = 0
n = 0
for i in range(len(a)):
 if a[i] > a[n]:
  n = i
 if a[i] < a[m]:
  m = i
a[m], a[n] = a[n], a[m]
print(' '.join([str(i) for i in a]))
