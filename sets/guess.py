"""Augustus and Beatrice play the following game. Augustus thinks of a secret integer number from 1 to n. Beatrice tries to guess the number by providing a set of integers. Augustus answers YES if his secret number exists in the provided set, or NO, if his number does not exist in the provided numbers. Then after a few questions Beatrice, totally confused, asks you to help her determine Augustus's secret number.
Given the value of n in the first line, followed by the a sequence Beatrice's guesses, series of numbers seperated by spaces and Agustus's responses, or Beatrice's plea for HELP. When Beatrice calls for help, provide a list of all the remaining possible secret numbers, in ascending order, separated by a space.
"""

n = int(input())
a = [i for i in range(1, n+1)]
s = set(a)
while True:
    guess = input()
    if guess == 'HELP':
        break
    answer = input()
    if answer == 'NO':
        s -= set(guess.split())
    elif answer == 'YES':
        s &= set(guess.split())
print(' '.join([str(i) for i in list(s)]))
