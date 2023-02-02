# # 26 с контейнерами
#
# # Открываем, считываем и сортируем файл
# f = open("data.txt")
# data = sorted([int(i) for i in f])
# f.close()
#
# # Создаём и инициализируем словарь (хеш-таблицу) в которой будем хранить количество каждого вида коробок
# cnt_boxes = dict()
# for i in data:
#     if i in cnt_boxes:
#         cnt_boxes[i] += 1
#     else:
#         cnt_boxes[i] = 1
#     # Another way:
#     # tmp = cnt_boxes.get(i, 0) + 1
#     # cnt_boxes[i] = tmp
#
# maximum = 0
# cnt_slots = 0
#
# while cnt_boxes:
#     current_box = list(cnt_boxes.keys())[0]  # Берём самую маленькую коробку которую можем взять
#     cnt_boxes[current_box] -= 1              # при этом количество этих коробок уменьшилось на одну (потому что мы её взяли)
#     cnt_current = 1                          # Теперь у нас одна коробка в руках
#     if cnt_boxes[current_box] == 0:          # Если количество коробок стало 0, то мы удаляем эту коробку
#         del cnt_boxes[current_box]
#
#     for i in list(cnt_boxes.keys()):         # Идём вдоль этого ряда коробок и ищем подходящую
#         if i - current_box >= 7:             # Если нашли подходящую коробку
#             current_box = i                  # Мы засунули маленькую коробку в эту и взяли большую коробку в руки
#             cnt_boxes[current_box] -= 1      # Количество этих коробок (которую мы взяли) уменьшилось на 1
#             cnt_current += 1                 # Теперь у нас на одну коробку в руках больше
#             if cnt_boxes[current_box] == 0:  # И снова, если количество коробок - 0, то удаляем эту коробку
#                 del cnt_boxes[current_box]
#
#     maximum = max(maximum, cnt_current)      # По задаче нужно найти сколько максимум можно положить коробок в коробку
#     cnt_slots += 1                           # Теперь мы заняли один слот
#
# print(cnt_slots, maximum)                    # Ура вывод
import math

# import turtle
#
# t = turtle.Pen()
# t.up()
# t.left(90)
# t.speed(1000)
# k = 100
#
#
# t.forward(100 * k)
# t.right(90)
# t.forward(100 * k)
# t.right(30)
# t.down()
# t.begin_fill()
# for i in range(4):
#     t.forward(25 * k)
#     t.right(90)
# t.end_fill()
#
# cnt = 0
# canvas = turtle.getcanvas()
#
# for x in range(-300 * k, 300 * k, k):
#     for y in range(-300 * k, 300 * k, k):
#         inters = canvas.find_overlapping(x, y, x, y)  # [5, 2, 3, 4, ]
#         if len(inters) == 1 and inters[0] == 5:
#             cnt += 1
#
# print(cnt)
#
# turtle.mainloop()

# 1 7620343
# 2 7620373
# 3 7620391
# 4 7620407
# 5 7620421
# 6 7620427
# 7 7620443
# 8 7620449

# k = 1
# for i in range(7620342, 7620455):
#     cnt = 0
#     for j in range(2, int(i**0.5) + 1):
#         if i % j == 0:  # i = 36; j = 6
#             cnt += 1
#             if i // j != j:
#                 cnt += 1
#     if cnt == 0:
#         print(k, i)
#         k += 1

# for i in range(11_112, 14_948):
#     num = i * i
#     cnt = 0
#     for j in range(2, i + 1):
#         if num % j == 0:
#             cnt += 1
#             if num // j != j:
#                 cnt += 1
#     if cnt == 3:
#         print(i * i)

# for i in range(1_000_000, 1_100_001):
#     dividers = [i]
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             dividers.append(j)
#             if (i // j) != j:
#                 dividers.append(i // j)
#
#     divs_ch = list(filter(lambda x: x % 2 == 0, dividers))
#
#     # divs_ch = [i for i in dividers if i % 2 == 0]
#     #
#     # divs_ch = []
#     # for j in dividers:
#     #     if j % 2 == 0:
#     #         divs_ch.append(j)
#
#     if len(divs_ch) == 9:
#         dividers.sort()
#         print(i, dividers[-2])

# a = [i**2 for i in range(100) if i % 2 == 0]
#
# a = []
# for i in range(100):
#     if i % 2 == 0:
#         a.append(i**2)

# arr = ["Hello", "123", "1cat", "9gog", "rest", "896"]
# b = list(filter(lambda x: x.isdigit(), arr))
# print(arr)
# print(b)

# max_divs = 0
# max_number = 0
# for i in range(600_000, 700_001):
#     cnt = 2
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 2:
#             cnt += 1
#             if (i // j) != j:
#                 cnt += 1
#     if cnt > max_divs:
#         max_divs = cnt
#         max_number = i
#
# print(max_divs, max_number)

# for i in range(700_000, 10000000000000000000000000):
# k = 700_000
# while True:
#     k += 1
#     break

# import itertools
# for i in itertools.count(700_000):  # 700_000


# k = 0
# for i in range(700_000, 10000000000000000000000):
#     div_min = 0
#     div_max = 0
#
#     for j in range(2, int(i**0.5) + 1):
#         if i % j == 0:
#             div_min = j
#             div_max = i // j
#             break
#
#     F = div_max - div_min
#     if F != 0 and F % 5 == 0:
#         print(i, F)
#         k += 1
#
#     if k == 6:
#         break

# k = 0
# for i in range(530_670, 1000000000000000000):
#     div_min = 0
#     div_max = 0
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             div_min = j
#             div_max = i // j
#             break
#
#     M = div_max + div_min
#     if M % 8 == 4:
#         print(i, M)
#         k += 1
#
#     if k == 6:
#         break


# print(text)

# file = open("data.txt")
# text = file.read()
# file.close()
#
# cnt = 0
# maximum = 0
# for i in range(len(text)):    # ZZZZZXXXXZZZZZZXXZZZZZZZZXXXXXXXX
#     if text[i] == "X":
#         cnt += 1
#     else:
#         maximum = max(maximum, cnt)
#         cnt = 0
#
# print(max(maximum, cnt))

# import re
#
# file = open("data.txt")
# text = file.read()
# file.close()
#
# print(
#     len(
#         max(
#             re.findall("X+", text),
#             key=len
#         )
#     )
# )

# A+ - 1 или больше вхождений А
# A* - 0 или больше вхождений А
# A? - 0 или 1 вхождение А
# [A, B, C] [A-Za-z] [0-9] [А-Яа-я] [A-Za-z0-9]
# [A-Z]+ - 1 или больше вхождение латинской заглавной буквы
#

# file = open("24_2.txt")
# text = file.read()
# file.close()
#
# cnt = 0
# maximum = 0
# for i in range(len(text)):
#     if text[i] != "X":
#         cnt += 1
#     else:
#         maximum = max(maximum, cnt)
#         cnt = 0
#
# print(max(maximum, cnt))  # 24

# file = open("24_2.txt")
# text = file.read().split("X")  # YZYYZYZYYZYZ  split(N) - разделить по подстроке N
# file.close()
#
# print(len(max(text, key=len)))  # 24
# YZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
# ZYYYYYYYYYY

# file = open("24_3.txt")
# text = file.read()
# file.close()
#
# cnt = 0
# maximum = 0
# for i in range(len(text)):
#     # Way 1
#     if text[i] != "A" and text[i] != "F":
#         cnt += 1
#     else:
#         maximum = max(maximum, cnt)
#         cnt = 0
#
#     # Way 2
#     # if text[i] == "A" or text[i] == "F":
#     #     maximum = max(maximum, cnt)
#     #     cnt = 0
#     # else:
#     #     cnt += 1
#
# print(max(maximum, cnt))  # 20

# import statistics
#
# arr = [1, 3, 2, 5, 7, 1, 3, 2, 3, 3, 3, 6, 8, 100, 12, 2, 1, 1, 1]
#
# print(statistics.mean(arr))
# print(sum(arr) / len(arr))
#
# import operator
#
# print("X Y X^Y")
#
# for i in range(2):
#     for j in range(2):
#         # print(i, j, i == 1 and j != 1 or i != 1 and j == 1)
#         # print(i, j, operator.xor(i, j))
#         print(i, j, i^j)

# def add(n1, n2):
#     res = n1 ^ n2
#     corr = (n1 & n2) << 1
#     while corr:
#         temp = res
#         res = res ^ corr
#         corr = (corr & temp) << 1
#     return res
#
# print(add(5, -7))

# a = 1
# print(a)
# a = "Hello"
# print(a)

# a = [1, 2, 3]
# print(a)
# a.append(4)
# print(a)

# from string import digits
#
# file = open("24_4.txt")
# text = file.read()
# file.close()
#
# cnt = 0
# maximum = 0
# for i in range(len(text)):
#     if text[i] in digits[1::2]:  # Way 2: int(text[i]) % 2 != 0  Way 3: text[i] in "13579"
#         cnt += 1
#     else:
#         maximum = max(maximum, cnt)
#         cnt = 0
#
# print(max(maximum, cnt))  # 13

# file = open("24_5.txt")
# text = file.read()
# file.close()
#
# cnt = 0
# for i in range(len(text) - 2):
#     if (
#             text[i] == text[i+2] and
#             text[i+1] in "FDE" and
#             text[i+2] in "BCD" and
#             text[i+2] != text[i+1]
#     ):  # i i+1 i+2
#         cnt += 1
#
# print(cnt)  # 2417

# file = open("448249e7-9baa-4c99-9717-b3a4c4a210fc.txt")
# text = file.read()
# file.close()
#
# cnt = 1
# maximum = 0
# for i in range(len(text) - 1):  # XYXYXZYZXYY
#     if (
#             text[i] in "XYZ" and
#             text[i+1] in "XYZ" and
#             text[i] != text[i+1]
#     ):
#         cnt += 1
#     else:
#         maximum = max(maximum, cnt)
#         cnt = 1
#
# print(max(maximum, cnt))  # 15

# from string import digits
#
# file = open("6f44e6ab-be6c-4fbc-b22a-1bb75346e6b8.txt")
# text = file.read()
# file.close()
#
# cnt = 0
# maximum = 0
# for i in range(len(text)):
#     if text[i] in digits[1::2]:  # Way 2: text[i] in "13579"
#         cnt += 1
#     else:
#         maximum = max(maximum, cnt)
#         cnt = 0
#
# print(max(maximum, cnt))  # 3

# from string import digits, ascii_letters
# from random import choices

# file = open("521c145b-a2cb-40bf-aee9-69ff7ca29528.txt")
# text = file.read()
# file.close()

# print("".join(choices(digits + ascii_letters, k=10)))

# import pyautogui
# import time
#
# time.sleep(5)
#
# for i in range(10):
#     pyautogui.typewrite("Hello")
#     pyautogui.press("enter")
#     time.sleep(0.01)

# def f(n):
#     r = bin(n)[2:]
#     s = 0
#     # Way 1
#     # while n != 0:
#     #     s += n % 10
#     #     n //= 10
#     for i in str(n):  # "1234"
#         s += int(i)
#     # for i in range(0, 10):  # 1232345  -> 3 + 3 = 3 * (1 +  = 3 * k = i * k
#     #     s += i * str(n).count(str(i))
#     print(s)
#
# f(12345)

# import itertools
#
# a = itertools.product("12", repeat=20)  # 0111222111222111222120
# a_perms = set()
# for i in a:
#     if i.count("1") == 10 and i.count("2") == 10:
#         a_perms.add("".join(i))
#
# minn = 99999999999999999999999999999999999999999999999999999999
# for i in a_perms:
#     s = "0" + i + "0"
#     while "00" not in s:
#         s = s.replace("012", '30', 1)
#         if "011" in s:
#             s = s.replace("011", "20", 1)
#             s = s.replace("022", "40", 1)
#         else:
#             s = s.replace("01", "10", 1)
#             s = s.replace("02", "101", 1)
#     if s.count("1") == 7 and s.count("2") == 5:
#         minn = min(minn, s.count("3"))
#
# print(minn)

# for x in range(0, 37):
#     num1 = \
#         1 * 37 ** 3 + \
#         2 * 37 ** 2 + \
#         3 * 37 ** 1 + \
#         x * 37 ** 0
#     num2 = \
#         4 * 37 ** 3 + \
#         x * 37 ** 2 + \
#         5 * 37 ** 1 + \
#         9 * 37 ** 0
#     summ = num1 + num2
#     if summ % 36 == 0:
#         print(summ // 36)


# for i in range(10):
#     print("Hello")
#     if i == 5:
#         break
# else:
#     print("Wow")

# for A in range(-100, 150):
#     for x in range(1, 300):
#         for y in range(1, 300):
#             if ((144 % x == 0) <= (not (x, y))) or (x + y > 100) or (A - x > y):
#                 pass
#             else:
#                 break
#         else:
#             continue
#         break
#     else:
#         print(A)
#
# for A in range(-100, 120):
#     flag = True
#     for x in range(1, 300):
#         for y in range(1, 300):
#             if ((144 % x == 0) <= (not (x % y == 0))) or (x + y > 100) or (A - x > y):
#                 pass
#             else:
#                 flag = False
#                 break
#     if flag == True:
#         print(A)

# def f(n: int) -> int:
#     r = bin(n)[2:]
#     return n - int(r[1:], 2)
#
#
# arr = []
# for i in range(10, 1001):
#     arr.append(f(i))
#
# s = set(arr)
# print(arr)
# print(len(s))

# def f(n: int) -> int:
#     r = bin(n)[2:]
#     r = r[::-1]
#     return int(r, 2)
#
#
# for i in range(1, 100):
#     if f(i) == 13:
#         print(i)


# 88x4y_9 + 7x44y_11
# В записи чисел переменными x и y обозначены допустимые в данных системах счисления неизвестные цифры.
# Определите значения x и y, при которых значение данного арифметического выражения будет наименьшим и
# кратно 61. Для найденных значений x и y вычислите частное от деления значения арифметического выражения
# на 61 и укажите его в ответе в десятичной системе счисления.

# for x in "012345678":
#     for y in "012345678":
#         num1 = "88" + x + "4" + y
#         num2 = "7" + x + "44" + y
#         summa = int(num1, 9) + int(num2, 11)
#         if summa % 61 == 0:
#             print(summa // 61)

# for x in "012345678":
#     for y in "012345678":
#         num1 = \
#             8 * 37 ** 4 + \
#             8 * 37 ** 3 + \
#             x * 37 ** 2 + \
#             4 * 37 ** 1 + \
#             y * 37 ** 0

# a = 4 ** 2020 + 2 ** 2017 - 15
# a_bin = bin(a)[2:]
#
# print(a_bin.count("1"))

# a = 7 * 512 ** 120  - 6 * 64 ** 100 + 8 ** 210 - 255
# a_oct = oct(a)[2:]
# print(a_oct.count("0"))

# a = 4 ** 36 + 3 * 4 ** 20 + 4 ** 15 + 2 * 4 ** 7 + 49
# a_hex = set(hex(a)[2:])
# print(len(a_hex))

# def tri(n):
#     res = ""
#     while n != 0:
#         res += str(n % 3)
#         n //= 3
#     res = res[::-1]
#     return res
#
# a = 9**8 + 3 ** 5 - 9
# a_tri = tri(a)
# print(a_tri.count("2"))

# ДЕЛ(n, m) обозначает выражение "натуральное число n делится на натуральное число m без остатка"
# n % m == 0
# ДЕЛ(n, m) <=> n % m == 0
# ДЕЛ(A, x) <=> A % x == 0

# factorial (9! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9)

# def fact(n):
#     if n != 1:
#         return n * fact(n-1)  # рекурсия
#     else:
#         return 1
#
# print(fact(1000))

# fact(9)
# 9 * 8 * 7 * 6...
# 9 * fact(8)
# fact(n) = n * fact(n-1)

# def f(n):
#     return f(n)
#
# f(10)

# fact(10)  ->
# 10 * fact(9)
# 9 * fact(8)
# 8 * fact(7)

# F(1) = 1
# F(2) = 3
# F(n) = F(n–1) * n + F(n–2) * (n – 1) , при n >2

# def f(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 3
#     else:
#         return f(n-1) * n + f(n - 1) * (n - 1)
#
# print(f(0))
