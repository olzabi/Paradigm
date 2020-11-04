print("\ntask6")

h = int(input("h = "))
m = int(input("m = "))
s = int(input("s = "))

general_hours = h * 30  # получаем градусы часовой стрелки
general_minutes = m * 6   # градусы МС

print("We have " + str(abs((general_hours + m * 0.5) - general_minutes)) + " degrees between hour and minute hands")

