from collections import Counter

first = input("first word?")
second = input("second word?")


def check_func(a, b):
    return Counter(a) == Counter(b)


print(check_func(first, second))
