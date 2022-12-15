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
