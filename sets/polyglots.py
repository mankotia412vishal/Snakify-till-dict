"""Each student at a certain school speaks a number of languages. We need to determine which languges are spoken by all the students, which languages are spoken by at least one student.
Given, the number of students, and then for each student given the number of languages they speak followed by the name of each language spoken, find and print the number of languages spoken by all the students, followed by a list the languages by name, then print the number of languages spoken by at least one student, followed by the list of the languages by name. Print the languages in alphabetical order.
"""

n = int(input())  # количество учеников
lang_nums = [0] * n  # количество языков для каждого ученика
langs = []  # наименования языков, для каждого из учеников
for i in range(n):
    lang_nums[i] = int(input())
    l = set()
    for j in range(lang_nums[i]):
        l.add(input())
    langs.append(l)
uni = set.union(*langs)
inter = set.intersection(*langs)
print(len(inter), '\n'.join(sorted(inter)), len(
    uni), '\n'.join(sorted(uni)), sep='\n')
