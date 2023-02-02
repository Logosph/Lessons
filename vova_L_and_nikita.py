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

# a = 100
# b = 30
#
# a_bin = bin(a)[2:]
# b_bin = bin(b)[2:]
#
# print(a_bin)
# print("00"+b_bin)  # 100 = 4
#
# print(a & b)


# Найти самую длинную последовательность из В
# a = "ABBAABABABBBABBBBABBABABABABBBAAABABBABAAAABBABAAAAAAA"
# maxx = 0
# cnt = 0
# for i in a:
#     if i == "A":
#         cnt += 1
#     else:
#         maxx = max(maxx, cnt)
#         cnt = 0
# print(max(maxx, cnt))

# Найти самую длинную последовательность ABABA...

# a = "ABABABABAAABABBBBABABBABABABABABABABABBAAABABABABABABABBABABA"
# XYZXYZXYZXYZ

# maxx = 0
# cnt = 1
# # Way 1
# for i in range(1, len(a)):
#     if a[i] != a[i - 1]:
#         cnt += 1
#     else:
#         maxx = max(maxx, cnt)
#         cnt = 1
#
# print(max(maxx, cnt))

# maxx = 0
# cnt = 1
# # Way 2
# for i in range(0, len(a) - 1):
#     if a[i] != a[i + 1]:
#         cnt += 1
#     else:
#         maxx = max(maxx, cnt)
#         cnt = 1

# a = "ABABABABAAABABBBBABABBAABABABABABABABABBAAABABABABABABABBABABA"
# maxx = 0
# cnt = 0
# for i in range(0, len(a)):
#     if cnt == 0 and a[i] == "A":
#         cnt = 1
#     elif cnt != 0 and (a[i] != a[i - 1]):
#         cnt += 1
#     else:
#         maxx = max(maxx, cnt)
#         if a[i] == "A":
#             cnt = 1
#         else:
#             cnt = 0
#
# print(max(maxx, cnt))

# a = "XYZXYZXYZXYXYYXYZYXZYXYZXYZXYZXYZXYZXYZXZYZYXYZYXYZXYZXYZXY"  # заменить XYZ на какой-то символ
#
# a = a.replace("XYZ", "!")  # 6 * 3 = 18
# maxx = 0
# cnt = 0
# for i in a:
#     if i == "!":
#         cnt += 1
#     else:
#         maxx = max(maxx, cnt)
#         cnt = 0
#
# print(max(maxx, cnt))
#
# f = open("24_demo (5).txt")
# text = f.read()
# f.close()
#
# cnt = 0  # XYZXYZXYZXYZ -> X - 0 3 6 9 - %3 == 0; Y - 1 4 7 10 - %3 == 1; Z - 2 5 8 11 - %3 == 2 YYZXYZXYZXYZ
# mx = 0
#
# for i in range(len(text)):
#     if (
#         text[i] == "X" and cnt % 3 == 0 or
#         text[i] == "Y" and cnt % 3 == 1 or
#         text[i] == "Z" and cnt % 3 == 2
#     ):
#         cnt += 1
#     else:
#         mx = max(mx, cnt)
#         cnt = 0
#
# print(max(mx, cnt))

# print("XYZXYZXYZXYZX" in text)

# text = text.replace("XYZ", "*")
# cnt = 0
# mx = 0
# for i in range(len(text)):
#     if text[i] == "*":
#         cnt += 1
#     else:
#         mx = max(mx, cnt)
#         cnt = 0
# print(max(mx, cnt))
#
#
# print(text)  # **** == XYZXYZXYZXYZ


# file = open("inf_22_10_20_24 (1).txt")
# cnt = 0
#
# for i in file:
#     if i.count("E") > i.count("A"):
#         cnt += 1
#
# print(cnt)
# file.close()

# Другие способы (они никому не понравились)
# file = open("inf_22_10_20_24 (1).txt")
# cnt = 0
# string = file.readline()
#
# while string:
#     if string.count("E") > string.count("A"):
#         cnt += 1
#     string = file.readline()
#
# print(cnt)
# file.close()
#
#
# file = open("inf_22_10_20_24 (1).txt")
# text = file.readlines()
# file.close()
#
# cnt = 0
# for i in range(len(text)):
#     if text[i].count("E") > text[i].count("A"):
#         cnt += 1
#
# print(cnt)
#
#
# file = open("inf_22_10_20_24 (1).txt")
# text = file.readlines()
# file.close()
#
# cnt = 0
# for i in text:
#     if i.count("E") > i.count("A"):
#         cnt += 1
#
# print(cnt)

# file = open("24 (2).txt")
# text = file.read()
# file.close()
#
# cnt = [0] * 26
#
# for i in range(len(text) - 1):
#     if text[i] == "A":
#         cnt[ord(text[i+1]) - ord("A")] += 1  # ord("A") = 65
#
# print(cnt)
# print(cnt.index(max(cnt)))  # g
# print(chr(cnt.index(max(cnt)) + ord("A")))  # g
#
# file = open("24 (2).txt")
# text = file.read()
# file.close()
#
# d = {}  # key: value
#
# for i in range(len(text) - 1):
#     if text[i] == "A":
#         d[text[i + 1]] = d.get(text[i + 1], 0) + 1
#
# mx = "A"
# for i in d:
#     if d[i] > d[mx]:
#         mx = i
#
# print(mx)

# print(max(d, key=d.get))

# d = {
#     "cat":      1,
#     2:          ["dog", "cat", "duck"],
#     True:       "15",
#     False:      16,
#     (1, 2, 3):  [4, 5, 6]
# }
#
# print(d.get(2, 0)[2])

# file = open("24 (2).txt")
# str_min_g = file.readline()
#
# for i in file:
#     if i.count("G") < str_min_g.count("G"):
#         str_min_g = i
#
# d = {}
#
# for i in range(len(str_min_g)):
#     d[str_min_g[i]] = d.get(str_min_g[i], 0) + 1
#
# mx_letter = "A"
# for i in d:
#     if d[i] >= d[mx_letter]:
#         if d[i] == d[mx_letter] and i > mx_letter or d[i] > d[mx_letter]:
#             mx_letter = i
#
# print(mx_letter)

# file = open("24 (2).txt")
# str_min_g = file.readline()
#
# # Поиск строки с минимальным количеством букв G
# for i in file:
#     if i.count("G") < str_min_g.count("G"):
#         str_min_g = i
#
# # Подсчёт количества всех букв
# a = [0] * 26
# for i in range(len(str_min_g) - 1):
#     a[ord(str_min_g[i]) - ord("A")] += 1
#
# # Поиск буквы которая встречается чаще всего
# mx = 0
# mx_index = 0
# for i in range(len(a)):
#     if a[i] >= mx:
#         mx = a[i]
#         mx_index = i
#
# print(chr(mx_index + ord("A")))


# Обозначим через m & n поразрядную конъюнкцию неотрицательных целых чисел m и n.
# Так, например, 14 & 5 = 1110_2 & 0101_2 = 0100_2 = 4.
# Для какого наименьшего неотрицательного целого числа А формула
# x & 29 ≠ 0 → (x & 17 = 0 → x & А ≠ 0)  # 29 17
# тождественно истинна (т.е. принимает значение 1 при любом неотрицательном целом значении переменной x)?

# for A in range(0, 10000):
#     flag = True   # Флаг поднят
#     for x in range(0, 300):  # Показать, что будет, если взять перебор слишком большим
#         if (x & 29 != 0) <= ((x & 17 == 0) <= (x & A != 0)):
#             pass
#         else:
#             flag = False  # Флаг опущен
#
#     if flag == True:
#         print(A)
#         break


# Для какого наименьшего неотрицательного целого числа А формула
# x&25 ≠ 0 → (x&17 = 0 → x&А ≠ 0)
# тождественно истинна (т.е. принимает значение 1 при любом неотрицательном целом значении переменной х)?

# for A in range(0, 10000):
#     flag = True
#     for x in range(0, 300):
#         if (x & 25 != 0) <= ((x & 17 == 0) <= (x & A != 0)):
#             pass
#         else:
#             flag = False
#
#     if flag == True:
#         print(A)
#         break

# Для какого наибольшего целого числа А формула
# ((x ≤ 9) →(x ⋅ x ≤ A)) ⋀ ((y ⋅ y ≤ A) → (y ≤ 9))
# тождественно истинна, то есть принимает значение 1 при любых целых неотрицательных x и y?

# for A in range(0, 10000):
#     flag = True
#     for x in range(300):
#         for y in range(300):
#             if ((x <= 9) <= (x * x <= A)) and ((y * y <= A) <= (y <= 9)):
#                 pass
#             else:
#                 flag = False
#     if flag:
#         print(A)

# ¬ДЕЛ(x, А) → (ДЕЛ(x, 6) → ¬ДЕЛ(x, 4))
for A in range(1, 10000):
    flag = True
    for x in range(1, 1000):
        if (not (x % A == 0)) <= ((x % 6 == 0) <= (x % 4 != 0)):
            pass
        else:
            flag = False
    if flag:
        print(A)
# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
# n % m == 0
