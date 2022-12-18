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

table = [[0 for j in range(10001)] for i in range(10001)]
f = open("data.txt")
for i in f:
    row = int(i.split()[0])  # ["8751", "1661"] '8751 1661'
    column = int(i.split()[1])
    table[row][column] = 1

cnt = 0
maximum = 0
max_row = 0
for i in range(10001):
    cnt = 0
    for j in range(10001):
        if table[i][j] == 1:
            cnt += 1
        else:
            if cnt > maximum:
                maximum = cnt
                max_row = i
            cnt = 0
    if cnt > maximum:
        maximum = cnt
        max_row = i

print(maximum, max_row)

