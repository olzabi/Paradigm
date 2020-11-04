num = int(input("task 1, number: "))
count = 1

for i in range(2, num + 1):
    count *= i

print(' Factorial of {0} is {1}'.format(num, count))
