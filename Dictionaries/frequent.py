# Given the text: the first line contains the number of lines, then given the lines of words. Print the word in the text that occurs most often. If there are many such words, print the one that is less in the alphabetical order.
counter = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1

max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
print(min(most_frequent))
