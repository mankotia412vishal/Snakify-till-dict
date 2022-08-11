"""Alice and Bob like to play with colored cubes. Each child has its own set of cubes and each cube has a distinct color, but they want to know how many unique colors exist if they combine their block sets. To determine this, the kids enumerated each distinct color with a random number from 0 to 108. At this point their enthusiasm dried up, and you are invited to help them finish the task.
Given two integers that indicate the number of blocks in Alice's and then Bob's sets N and M. The following N lines contain the numerical color value for each cube in Alice's set. Then the last M rows contain the numberical color value for each cube in Bob's set.

Find three sets: the numerical colors of cubes in both sets, the numerical colors of cubes only in Alice's set, and the numerical colors of cubes only in Bob's set. For each set, print the number of elements in the set, followed by the numerical color elements, sorted in ascending order.
"""

n, m = [int(j) for j in input().split()]
A = set()
B = set()
for i in range(n):
    A.add(int(input()))
for i in range(m):
    B.add(int(input()))
C = A & B
D = A - B
Е = B - A
print(len(C))
print(*sorted(C), key=int)
print(len(D))
print(*sorted(D), key=int)
print(len(Е))
print(*sorted(Е), key=int)
