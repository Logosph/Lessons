# Lists comprehension
# a = []  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(10):
#     a.append(i)
# arr = [<то, что будем добавлять> for i in <то что будем перебирать> <условия>]
# a = [i for i in range(10) if i % 3 != 0]
# print(a)


# Type 26 №22
# f = open("data.txt")
# data = [int(i) for i in f]
# # data = list(map(int, f.read().split()))
# f.close()
#
#
# cnt = 0
# maximum = 0
# data1 = set(data)
# for i in range(len(data) - 1):  # i = len(data) - 2  # [1, 2, 3] -> len = 3; ind_max = 2
#     for j in range(i + 1, len(data)):
#         if (
#             data[i] % 2 == 0 and
#             data[j] % 2 == 0
#         ):
#             if (data[i] + data[j]) // 2 in data1:
#                 cnt += 1
#                 maximum = max(maximum, (data[i] + data[j]) // 2)
#
# print(cnt, maximum)

# set - множество
# Неупорядоченная коллекция уникальных объектов

# set1 = {5, 5, 5, 5, 5, 5, 5}
# print(set1)
# set2 = list({"a", "b", "c"})
# print(set2[1])
# set3 = {4, 1, 6, 2, 7, 8, 9, 2, 2, 3, 2, 10, 11, 23, 12}
# print(set3)

# Двумерные массивы

# a = [[j + i * 5 for j in range(5)] for i in range(5)]
# b = []
# for i in range(5):
#     c = []
#     for j in range(5):
#         c.append(j + i * 5)
#     b += [c]

# for i in range(5):
#     for j in range(5):
#         print(f'{a[i][j]: ^3}', end=" ")
#     print()

# print()
#
# for i in range(5):
#     for j in range(5):
#         print(f'{b[i][j]: ^3}', end=" ")
#     print()

# a = [[j + i * 5 for j in range(5)] for i in range(5)]
# print(a[0][3])
# for i in range(5):
#     for j in range(5):
#         print(f'{a[i][j]: ^3}', end=" ")
#     print()

# table = [[0 for j in range(10001)] for i in range(10001)]
# f = open("data.txt")
# for i in f:
#     row = int(i.split()[0])  # ["8751", "1661"] '8751 1661'
#     column = int(i.split()[1])
#     table[row][column] = 1
#
# cnt = 0
# maximum = 0
# max_row = 0
# for i in range(10001):
#     cnt = 0
#     for j in range(10001):
#         if table[i][j] == 1:
#             cnt += 1
#         else:
#             if cnt > maximum:
#                 maximum = cnt
#                 max_row = i
#             cnt = 0
#     if cnt > maximum:
#         maximum = cnt
#         max_row = i
#
# print(maximum, max_row)

# table = []
# for i in range(10001):
#     table.append([0] * 10001)
#
# file = open("data.txt")
# text = [i for i in file]
# file.close()
#
# for i in text:  # "123 12".split() -> ["123", "12"]
#     x = int(i.split()[0])
#     y = int(i.split()[1])
#     table[x][y] = 1
#
# maximum = 0
# max_row = 0
# cnt = 0
# for i in range(len(table)):
#     for j in range(len(table[i])):
#         if table[i][j] == 1:
#             cnt += 1
#         else:
#             if cnt > maximum:
#                 maximum = cnt
#                 max_row = i
#             cnt = 0
#
# print(max(maximum, cnt), max_row)

# arr = [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
# cnt = 0
# maximum = 0
# for i in range(len(arr)):
#     if arr[i] == 1:
#         cnt += 1
#     else:
#         maximum = max(maximum, cnt)
#         cnt = 0
#
# print(max(cnt, maximum))

# ((x ≤ 9) →(x ⋅ x ≤ A)) ⋀ ((y ⋅ y ≤ A) → (y ≤ 9))

# for A in range(1, 10000):
#     for x in range(300):
#         for y in range(300):
#             if  ((x <= 9) <= (x * x <= A)) and ((y * y <= A) <= (y <= 9)): # <= == импликация 1 0 00 01 11
#                 pass
#             else:
#                 break
#         else:
#             continue
#         break
#     else:
#         print(A)

# for A in range(1, 10000):
#     suitable = True
#     for x in range(300):
#         for y in range(300):
#             if  ((x <= 9) <= (x * x <= A)) and ((y * y <= A) <= (y <= 9)):
#                 pass
#             else:
#                 suitable = False
#     if suitable:
#         print(A)


# for i in range(10):
#     pass
# else:
#     print("2")
#
# print("1")

# x & 29 ≠ 0 → (x & 17 = 0 → x & А ≠ 0)

# for A in range(1000):
#     for x in range(300):
#         if (x & 29 != 0) <= ((x & 17 == 0) <= (x & A != 0)):
#             pass
#         else:
#             break
#     else:
#         print(A)

a = 100
b = 30

a_bin = bin(a)[2:]
b_bin = bin(b)[2:]

print(a_bin)
print("00"+b_bin)  # 100 = 4

print(a & b)
