import random as r

N = int(input("choose from 1 to 5? "))

matrix = [[r.randint(0, 30) for i in range(N)] for j in range(N)]
print(matrix)

max_list = [max(i) for i in matrix]
max_value = max(max_list)
maximal_i = max_list.index(max(max_list))
print(max_list)
print(maximal_i)
