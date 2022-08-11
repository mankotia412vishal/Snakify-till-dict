# Given a positive real number a and a non-negative integer n. Calculate an without using loops, ** operator or the built in function math.pow(). Instead, use recursion and the relation an = a⋅an−1. Print the result.
# Form the function power(a, n).


def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


print(power(float(input()), int(input())))
