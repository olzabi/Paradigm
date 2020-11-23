"""
------------------------------------
Используемый алгоритм - O(√n)
тогда √n = n*n
------------------------------------
"""
is_prime = int(input())

d = 2
while d * d <= is_prime and is_prime % d != 0:
    d += 1
print(d * d > is_prime)
