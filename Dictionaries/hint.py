"""Given a number n, followed by n lines of text, print all words encountered in the text, one per line. The words should be sorted in descending order according to their number of occurrences in the text, and all words with the same frequency should be printed in lexicographical order.
Hint. After you create a dictionary of the words and their frequencies, you would like to sort it according to the frequencies. This can be achieved if you create a list whose elements are tuples of two elements: the frequency of occurrence of a word and the word itself. For example, [(2, 'hi'), (1, 'what'), (3, 'is')]. Then the standard list sort will sort a list of tuples, with the tuples compared by the first element, and if these are equal, by the second element. This is nearly what is required in the problem.
"""

counter = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1

for i in sorted(counter.items(), key=lambda x: (-x[1], x[0])):
    print(i[0])
