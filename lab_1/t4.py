print("\ntask4")

number = input("Choose three-digit number: ")
tmp = number

number_list = list(number)
number_list.reverse()
number = "".join(number_list)

print("The reversed number of {} is ".format(tmp) + number)

"""
tmp = tmp[::-1]
print("Второй вариант через срез:" + tmp)
"""