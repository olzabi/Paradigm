
def is_prime(number):
    j = 2
    while j * j <= number and number % j != 0:
        j += 1
    return print(j * j > number)


is_prime(5)
