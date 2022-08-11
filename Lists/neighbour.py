# Given a list of numbers, find and print the first adjacent elements which have the same sign.
#  If there is no such pair, leave the output blank.


a = [int(i) for i in input().split()]
for i in range(1, len(a)):
 if a[i-1]*a[i] > 0:
  print(a[i-1], a[i])
  break
