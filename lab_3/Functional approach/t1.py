num = int(input("number: "))


def factorial(number):
    if number == 0:
        return 1
    return factorial(number - 1) * number


print('Factorial of number {0} is {1}'.format(num, factorial(num)))
