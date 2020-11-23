import random as r

N = int(input("choose from 1 to 5? "))

matrix = [[r.randint(0, 30) for i in range(N)] for j in range(N)]
maximum = [max(i) for i in matrix]

print(matrix)
print(max(maximum))
