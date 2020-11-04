
print("\ntask8")

number = int(input("Your number? "))
res = number % 7
res = 7 if res == 0 else res
print("The selected number is {} day".format(res))
