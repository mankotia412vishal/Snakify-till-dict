"""Write a function capitalize(lower_case_word) that takes the lower case word and returns the word with the first letter capitalized. Eg., print(capitalize('word')) should print the word Word.
Then, given a line of lowercase ASCII words(text separated by a single space), print it with the first letter of each word capitalized using the your own function capitalize().

In Python there is a function ord(character), which returns character code in the ASCII chart, and the function chr(code), which returns the character itself from the ASCII code. For example, ord('a') == 97, chr(97) == 'a'
"""


def capitalize(word):
    return chr(ord(word[0]) + ord('A') - ord('a')) + word[1:]


s = [str(s) for s in input().split()]
for i in range(len(s)):
    s[i] = capitalize(s[i])
print(' '.join([str(i) for i in s]))
