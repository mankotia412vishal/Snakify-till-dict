"""Given a list of countries and cities of each country. Then given the names of the cities. For each city specify the country in which it is located.
"""

n = int(input())
cities = {}
for _ in range(n):
    line = input().split()
    for city in line[1:]:
        cities[city] = line[0]

for _ in range(int(input())):
    print(cities[input()])
