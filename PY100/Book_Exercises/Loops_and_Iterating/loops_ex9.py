# Write a function that computes and returns the factorial of a number by using a for or while loop. The factorial of a positive integer n, signified by n!, is defined as the product of all integers between 1 and n, inclusive


def factorial(n):
    result = 1
    for num in range(1, n + 1):
        result *= num

    return result


print(factorial(1))  # 1
print(factorial(2))  # 2
print(factorial(3))  # 6
print(factorial(4))  # 24
print(factorial(5))  # 120
print(factorial(6))  # 720
print(factorial(7))  # 5040
print(factorial(8))  # 40320
print(factorial(25))  # 15511210043330985984000000
