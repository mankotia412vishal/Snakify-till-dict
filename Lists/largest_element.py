# Given a list of numbers. Determine the element in the list with the largest value.
#  Print the value of the largest element and then the index number. 
#  If the highest element is not unique, print the index of the first instance.


b=0
a=[int(i) for i in input().split()]
for i in range(len(a)):
 if a[i] > a[b]:
  b=i
print(a[b],b)