def factorial(n):
    temp = 1
    print("temp variable type:", type(temp))
    for i in range(1, n + 1):
        temp *= i
    return temp


print("factorial variable type:", type(factorial))
print(factorial(5))
print(factorial(0))
