# Given a positive real number a and integer n.
# Compute an. Write a function power(a, n) to calculate the results 
# using the function and print the result of the expression.

# Don't use the same function from the standard library.


def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res


print(power(float(input()), int(input())))
