# Given a list of numbers with all of its elements sorted in ascending order, 
# determine and print the quantity of distinct elements in it.


a = [int(i) for i in input().split()]
n = 1
for i in range(0, len(a)-1):
 if a[i] != a[i + 1]:
   n += 1
print(n)
