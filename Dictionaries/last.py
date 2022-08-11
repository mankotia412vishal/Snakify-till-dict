from collections import defaultdict

lte = defaultdict(list)
for i in range(int(input())):
    ew, ltc = input().split(' - ')
    lt = ltc.split(', ')
    for lw in lt:
        lte[lw].append(ew)

print(len(lte))
for lw, et in sorted(lte.items()):
    print(lw + ' - ' + ", ".join(et))
