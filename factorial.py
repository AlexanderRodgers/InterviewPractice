

'''
Given a number n, compute the value of n! (n factorial).
'''
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    return n

print(factorial(6))

def factorial_2(n):
    x = 1
    factorial = 1
    while (x <= n):
        factorial = factorial * x
        x += 1
    return factorial

print(factorial_2(6))

def factorial_3(n):
    return n if n == 1 else n * factorial_3(n - 1)

print(factorial_3(6))