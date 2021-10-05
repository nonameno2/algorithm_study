# 1. recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input())
print(factorial(n))


# 2. for loop
def factorial():
    result = 1
    if n > 0: 
        for i in range(1, n + 1):
            result *= i
    return result

n = int(input())
print(factorial())
