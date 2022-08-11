# Given a list of numbers, find and print all the list
#  elements with an even index number. (i.e. A[0], A[2], A[4], ...).
# # 


a=input().split()
for i in range(0,len(a),2):
 print(a[i],end=" ")