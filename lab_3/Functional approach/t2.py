import random as r

'''
была попытка сделать 2 задание с матрицами через генераторы
'''

N = int(input("choose from 1 to 5? "))

matrix = [[r.randint(0, 30) for i in range(N)] for j in range(N)]
max_list = [max(i) for i in matrix]

z = max(max_list)
# for z in matrix:


max_value = max(max_list)
maximal_i = max_list.index(max(max_list))


print(matrix)  # 1+
print(max_list)
print(maximal_i)
