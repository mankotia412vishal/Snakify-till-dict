# Given a list of numbers,

#  count how many element pairs have the same value(are equal). 
#  Any two elements that are equal to each other should be counted exactly once.


a = [int(s) for s in input().split()]
c = 0
for i in range(len(a)):
 for j in range(i + 1, len(a)):
  if a[i] == a[j]:
   c += 1
print(c)
