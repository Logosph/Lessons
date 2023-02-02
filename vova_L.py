# Алгоритм получает на вход натуральное число N>1 и строит
# по нему новое число R следующим образом:
# 
# 1. Строится двоичная запись числа N.
# 2. Вычисляется количество единиц, стоящих на чётных местах в
# двоичной записи числа N без ведущих нулей, и количество нулей,
# стоящих на нечётных местах. Места отсчитываются слева направо
# (от старших разрядов к младшим, начиная с единицы).
# 3. Результатом работы алгоритма становится модуль разности полученных двух чисел.
# 
# Пример. Дано число N=39. Алгоритм работает следующим образом:
# 1.Строится двоичная запись: 3910=1001112.
# 2.Выделяем единицы на чётных и нули на нечётных местах: 100111.
# На чётных местах стоят две единицы, на нечётных— один ноль.
# 3.Модуль разности равен 1.
# Результат работы алгоритма R=1.
# При каком наименьшем N в результате работы алгоритма получится
# R=4?

# def f(n):
#     r = bin(n)[2:]
#     cnt_1 = 0
#     cnt_0 = 0
#     for i in range(0, len(r), 2):
#         if r[i] == "0":
#             cnt_0 += 1
#     for i in range(1, len(r), 2):
#         if r[i] == "1":
#             cnt_1 += 1
#
#     return abs(cnt_1 - cnt_0)
#
#
# for i in range(1, 10000):
#     if f(i) == 4:
#         print(i)
#         break

# def f(n):
#     r = bin(n)[2:]
#     r += str(r.count("1") % 2)
#     r += str(r.count("1") % 2)
#     return int(r, 2)
#
#
# for i in range(1, 10000):
#     if f(i) > 43:
#         print(f(i))
#         break

# and, or, xor, ==, -->
# и      and
# но      and                   А(у квадрата 4 стороны,) но Б(у треугольника две стороны) = ложь
# хотя бы      or
# только одно      xor
# если ... то     -->
# тогда и только тогда когда     ==
# а      and
# либо... либо...     xor

# xor - исключающеее ИЛИ
# A B F
# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 0


# file = open("data.txt")
# data = [int(i) for i in file]  # -67, -694, 835, 786, -457, 495, -699, -592, -405, -745, 656
# file.close()
#
# cnt = 0  # cnt - count
# mx = 0
# for i in range(len(data) - 1):
#     if data[i] % 3 == 0 or data[i + 1] % 3 == 0:
#         cnt += 1
#         mx = max(mx, data[i] + data[i + 1])
#
# print(cnt, mx)
#
# file = open("data.txt")
# data = [int(i) for i in file]  # 5500, 6971, 3572, 7600, 2822, 5687, 9741, 8623, 7954, 1029, 9913, 380, 7965, 3679,
# file.close()
#
# d = 160
# p = 7
#
# cnt = 0
# mx = 0
#
# for i in range(len(data) - 1):
#     for j in range(i + 1, len(data)):
#         if data[i] % d != data[j] % d and (data[i] % p == 0 or data[j] % p == 0):
#             cnt += 1
#             mx = max(mx, data[i] + data[j])
#
# print(cnt, mx)

# for a in range(300):
#     flag = True
#     for x in range(500):
#         for y in range(500):
#             if not ((y + 2 * x < a) or (x > 15) or (y > 30)): #  (y + 2x < A) ∨ (x > 15) ∨ (y > 30)
#                 flag = False
#     if flag:
#         print(a)
#         break

# a -> b
# not a or b

# 10 единиц 4 двойки

# a = "1234"
# a_perms = itertools.permutations(a)
# a_prod = itertools.product(a ,repeat=3)
# print(list(a_perms))
# print(list(a_prod))

# import itertools
#
# a_arr = set()
# for i in itertools.product("12", repeat=14):
#     s = "".join(i)
#     if s.count("1") == 10 and s.count("2") == 4:
#         a_arr.add(s)
#
# mx = 0
# for a0 in a_arr:
#     a = a0
#     while "11" in a:
#         if "112" in a:
#             a = a.replace("112", "6", 1)
#         else:
#             a = a.replace("11", "3")
#     s = 0
#     for i in a:
#         s += int(i)
#     mx = max(mx, s)
#
# print(mx)
#
# count = 0
# f = open('9.txt')
# for s in f:
#     arr = list(map(int, s.split()))
#     rep = sum(arr) - sum(set(arr))
#     mean_unrep = sum(set(arr) - {rep}) / 4
#     if len(set(arr)) == 5 and mean_unrep <= 2 * rep:
#         count += 1
# print(count)

# import turtle
# t = turtle.Pen()
# t.left(90)
# t.down()
# k = 100
# t.speed(10000000)
#
# t.begin_fill()
# for i in range(2):  # Настроить такое количество повторений, чтобы фигура рисовалась только один раз
#     t.forward(10 * k)
#     t.right(60)
#     t.forward(10 * k)
#     t.right(120)
# t.end_fill()
#
# canvas = turtle.getcanvas()
# cnt = 0
# for x in range(-300 * k, 300 * k, k):
#     for y in range(-300 * k, 300 * k, k):
#         tmp = canvas.find_overlapping(x, y, x, y)
#         if tmp == (5, ):
#             cnt += 1
#
# print(cnt)
# turtle.mainloop()

# Сколько слов длины 5, начинающихся с гласной буквы, можно составить из букв Е, Г, Э?
# Каждая буква может входить в слово несколько раз.
# Слова не обязательно должны быть осмысленными словами русского языка.

# import itertools
# a = itertools.product("ЕГЭ", repeat=5)
# a_strs = []
# for i in a:
#     s = "".join(i)
#     a_strs.append(s)
#
# cnt = 0
# for i in a_strs:
#     if i[0] in ("Е", "Э"):
#         cnt += 1
#
# print(cnt)

# Вася составляет 5-буквенные слова, в которых есть только буквы С, Л, О, Н, причём буква С используется
# в каждом слове ровно 1 раз. Каждая из других допустимых букв может встречаться в слове любое количество
# раз или не встречаться совсем. Словом считается любая допустимая последовательность букв, не обязательно
# осмысленная. Сколько существует таких слов, которые может написать Вася?

# import itertools
#
# def f(n):
#     return n.count("С") == 1
#
# a = itertools.product("СЛОН", repeat=5)
# a_strs = []
# for i in a:
#     a_strs.append("".join(i))
#
# # map
# # filter
# # zip
#
# a_filtered = list(filter(f, a_strs))
# print(len(a_filtered))

# a = ["1", "12", "234"]
# a_int = list(map(int, a))
# print(a)
# print(a_int)

# Полина составляет 6-буквенные коды из букв П, О, Л, И, Н, А.
# Каждую букву нужно использовать ровно 1 раз, при этом нельзя ставить подряд две гласные или две согласные.
# Сколько различных кодов может составить Полина?

# import itertools
# a = itertools.permutations("ПОЛИНА")
# a_strs = []
# for i in a:
#     a_strs.append("".join(i))
#
# cnt = 0
# for i in a_strs:
#     if (
#         "ОИ" not in i and
#         "ИО" not in i and
#         "ИА" not in i and
#         "АИ" not in i and
#         "АО" not in i and
#         "ОА" not in i and
#         "ПЛ" not in i and
#         "ЛП" not in i and
#         "ЛН" not in i and
#         "НЛ" not in i and
#         "ПН" not in i and
#         "НП" not in i
#     ):
#         cnt += 1
# print(cnt)

# for i in range(37):
#     n1 = 1 * 37 ** 3 + \
#          2 * 37 ** 2 + \
#          3 * 37 ** 1 + \
#          i * 37 ** 0
#     n2 = 4 * 37 ** 3 + \
#          i * 37 ** 2 + \
#          5 * 37 ** 1 + \
#          9 * 37 ** 0
#     summ = n1 + n2
#     if summ % 36 == 0:
#         print(summ // 36)


# def f(s1, s2, pos):
#     if s1+s2 >= 81 and pos == 3:
#         return True
#     elif s1 + s2 < 81 and pos == 3 or s1 + s2 >= 81:
#         return False
#     if pos % 2 == 1:
#         return f(min(s1, s2) + 1, max(s1, s2), pos+1) and f(min(s1, s2) + 2, max(s1, s2), pos+1) and f(min(s1, s2)*2, max(s1, s2), pos+1)
#     else:
#         return f(min(s1, s2) + 1, max(s1, s2), pos + 1) or f(min(s1, s2) + 2, max(s1, s2), pos + 1) or f(min(s1, s2) * 2, max(s1, s2), pos + 1)
#
# for i in range(1, 69):
#     if f(i, 12, 1):
#         print(i)

# Сколько существует шестизначных чисел, делящихся на 5, в которых каждая цифра может встречаться только
# один раз, при этом никакие две чётные и две нечётные цифры не стоят рядом.

# import itertools
#
# a = itertools.permutations("0123456789", r=6)
# a_strs = []
# for i in a:
#     a_strs.append("".join(i))
#
# cnt = 0
# for i in a_strs:
#     if i[-1] in "50" and i[0] != "0":
#         i0 = i\
#             .replace("0", "*")\
#             .replace("2", "*")\
#             .replace("4", "*")\
#             .replace("6", "*")\
#             .replace("8", "*")\
#             .replace("1", "$")\
#             .replace("3", "$")\
#             .replace("5", "$")\
#             .replace("7", "$")\
#             .replace("9", "$")
#         if "**" not in i0 and "$$" not in i0:
#             cnt += 1
#
# print(cnt)

# for i in range(10):
#     print("Hello" + str(i))
#
# for i in range(5):
#     print("LOL")
#
# print("for ended")
