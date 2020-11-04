input_str = input()


def reverse_this(string):
    return ''.join(map(lambda x: x+' ', string.split()[::-1]))


print(reverse_this(input_str))
