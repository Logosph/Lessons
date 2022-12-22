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
