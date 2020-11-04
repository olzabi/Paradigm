import math

print("\ntask3")

a = int(input("Choose 1st number "))
b = int(input("Choose 2nd number "))

# 3.1 среднее арифметическое двух чисел
arithmetic_formula = (a+b)/2
print("Arithmetic mean of numbers {0} and {1} is {2} ".format(a, b, arithmetic_formula))

# 3.2 среднее геометрическое двух чисел
geometric_formula = math.sqrt(a * b)
print("Geometric mean of numbers {0} and {1} is {2} ".format(a, b, geometric_formula))
