given_string = "The phrase seems to make sense but it makes no sense."
print("Given string: \n", given_string)

given_string = given_string.replace(".", "").split()
print("The last word is: ", given_string[-1])
max_len = max(len(i) for i in given_string[:-1])

for i in given_string[:-1]:
    if i == given_string[-1] or len(i) != max_len:
        given_string.remove(i)


result = ''.join(given_string[:-1])
print(result)
