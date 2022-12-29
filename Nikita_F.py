# def maximum(num1, num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2
#
#
# a = int(input())
# b = int(input())
# c = int(input())
#
# # if a > b:
# #     if a > c:
# #         print(a)
# #     else:
# #         print(c)
# # else:
# #     if b > c:
# #         print(b)
# #     else:
# #         print(c)
#
# print(maximum(maximum(a, b), c))

# from time import time
#
# def dividers_prime(num):
#     divs = []
#     for i in range(1, num+1):
#         if num % i == 0:
#             divs.append(i)
#
#     return divs
#
# def dividers_optimal(num: int) -> list[int]:
#     divs = [1, num]
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             divs.append(i)
#             if num // i != i:
#                 divs.append(num // i)
#     return sorted(divs)
#
# # start = time()
# # print(dividers_prime(36_000_000))
# # end = time()
# #
# # print(end - start)
#
# start = time()
# print(dividers_optimal(360_000_000_000_000))
# end = time()
#
# print(end - start)

# 36/1 < 36 / (1, 2) < 36/2

# from time import time
#
# def dividers_prime(num):
#     divs = []
#     for i in range(1, num+1):
#         if num % i == 0:
#             divs.append(i)
#
#     return divs
#
# def dividers_half(num):
#     divs = [1]
#     for i in range(2, num // 2 + 1):
#         if num % i == 0:
#             divs.append(i)
#     divs.append(num)
#     return divs
#
# def dividers_optimal(num: int) -> list[int]:
#     divs = [1, num]
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             divs.append(i)
#             if num // i != i:
#                 divs.append(num // i)
#     return sorted(divs)
#
# # Not optimal O(n)
# start = time()
# print(dividers_prime(36))
# end = time()
# print(end - start)
#
# # Half optimal O(n/2)
# start = time()
# print(dividers_half(36))
# end = time()
# print(end - start)
#
# # Optimal O(sqrt(n))
# start = time()
# print(dividers_optimal(36))
# end = time()
# print(end - start)

# import math
# n = 2.5
#
# print(math.ceil(n))  # Округляет вверх
# print(math.floor(n))  # Округляет вниз
# print(round(n))  # Округляет "математически"

# [174457; 174505]

# for i in range(174_457, 174_506):
#     dividers = []
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             dividers.append(j)
#             if i // j != j:
#                 dividers.append(i // j)
#     if len(dividers) == 2:
#         print(dividers, dividers[0] * dividers[1])

# Совершенное число
# for i in range(1, 1000000000000000000000000000000000):
#     dividers = [1]
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             dividers.append(j)
#             if i // j != j:
#                 dividers.append(i // j)
#     if sum(dividers) == i:
#         print(i)
# k = 1
# for i in range(245_690, 245_756):
#     dividers = []
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             dividers.append(j)
#             if i // j != j:
#                 dividers.append(i // j)
#     if len(dividers) == 0:
#         print(k, i)
#     k += 1

# def foo(x):
#     return x % 2 != 0
#
# for i in range(95632, 95651):
#     dividers = [1, i]
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             dividers.append(j)
#             if i // j != j:
#                 dividers.append(i // j)
#
#     divs_nechet = [k for k in dividers if k % 2 != 0]
#
#     # divs_nechet = list(filter(lambda x: x % 2 != 0, dividers))
#     #
#     # divs_nechet = []
#     # for k in dividers:
#     #     if i % 2 != 0:
#     #         divs_nechet.append(i)
#
#     if len(divs_nechet) == 6:
#         print(*sorted(divs_nechet))

# Перебрать все числа больше 1234 и остановиться после пяти чисел, кратных 6

# Way 1
# from itertools import count
#
# cnt = 0
# for i in count(1234):
#     if i % 6 == 0:
#         print("NUMBER", end=' ')
#         cnt += 1
#     print(i)
#     if cnt == 5:
#         break

# Way 2
# cnt = 0
# for i in range(1234, 99999999999999999999999999999999999999999999999999999):
#     if i % 6 == 0:
#         print("NUMBER", end=' ')
#         cnt += 1
#     print(i)
#     if cnt == 5:
#         break

# Way 3
# cnt = 0
# i = 1234
# while cnt < 5:
#     if i % 6 == 0:
#         print("NUMBER", end=' ')
#         cnt += 1
#     print(i)
#     i += 1
