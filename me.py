# Laboratorniy pr 1.02
# from statistics import mean
# data = {250 + i * 50: 0 for i in range(12)}
# with open("data.txt") as f:
#     for i in data:
#         data[i] = int(f.readline())
#
# print(" h   t   g ")
# for i in data:
#     print(f"{i:^3} {data[i]:^3} {2 * i * 10**-3 / ((data[i] * 10**-3)**2):.3f}")
#
# gs = [2 * i * 10**-3 / ((data[i] * 10**-3)**2) for i in data]
# g_avg = mean(gs)
#
# print(f"\ng avg = {g_avg:.4f}")

# LP 1.16
# from statistics import mean
#
#
# class Calcs:
#     H: int = 0
#     h: int = 0
#     G: float = 0
#
#     def __init__(self, H, h) -> None:
#         self.H = H
#         self.h = h
#         self.G = H / (H - h)
#
#
# table = []
# with open("data.txt") as f:
#     for i in f:
#         table.append(Calcs(int(i.split()[0]), int(i.split()[1])))
#
# G_avg = mean([i.G for i in table])
#
# print(f"G avg = {G_avg:.4f}\n")
#
# print(" № |  H  |  h  |   G   |  dG   |  dG^2 ")
# for num, i in enumerate(table):
#     print(f"{num: >2} | {i.H: ^3} | {i.h: ^3} | {i.G:.3f} | {abs(i.G - G_avg):.3f} | {abs(i.G - G_avg)**2:.3f} ")
#
# sqr_Gs = sum([abs(i.G - G_avg)**2 for i in table])
#
# print((sqr_Gs / 16 / 15 )**0.5 * 1.1)
#
# a = 9
# bit8 = f'{bin(a)[2:]:0>8}'
#
# print(bit8)

# def f(n):
#     if n < 3:
#         return n + 5
#     else:
#         return f(n-1) + 2 * g(n - 1) + 3 + g(n - 2)
#
# def g(n):
#     if n < 4:
#         return 2 * n
#     else:
#         return f(n-2) + g(n-1) - f(n-3)
#
#
# print(f(21))

# cnt = 0
# for A in range(1, 1000):
#     for x in range(100):
#         for y in range(100):
#             if not(((x >= 8) <= (x**2 >= A)) and ((y**2 >= A) <= (y >= 7))):
#                 break
#         else:
#             continue
#         break
#     else:
#         cnt += 1
#         print(A)
#
# print(cnt)


# def f(n) -> bool:
#     a = n != 2
#     b = 10
#     if a:
#         b //= 3
#     else:
#         b /= 4
#     return b

# def f(s, pos) -> bool:
#     if s >= 40 and pos in (3, 5):
#         return True
#     elif s >= 40 or s < 40 and pos == 5:
#         return False
#     if pos % 2 == 0:
#         return f(s + 1, pos + 1) or f(s + 2, pos + 1) or f(s * 2, pos + 1)
#     else:
#         return f(s + 1, pos + 1) and f(s + 2, pos + 1) and f(s * 2, pos + 1)
#
# def g(s, pos) -> bool:
#     if s >= 40 and pos == 3:
#         return True
#     elif s >= 40 or s < 40 and pos == 3:
#         return False
#     if pos % 2 == 0:
#         return f(s + 1, pos + 1) or g(s + 2, pos + 1) or g(s * 2, pos + 1)
#     else:
#         return g(s + 1, pos + 1) and g(s + 2, pos + 1) and g(s * 2, pos + 1)
#
# for i in range(1, 40):
#     if f(i, 1) and not g(i, 1):
#         print(i)

# import string
# import random
# from pyautogui import press, typewrite
# from time import sleep
#
# sleep(6)
#
# for i in range(498):
#     typewrite("spam")
#     press("enter")
#     sleep(0.05)

# print("".join(
#     random
#     .choices(
#         string.ascii_letters +
#         string.digits +
#         string.punctuation,
#         k=10
#     )
# ))

# string = '''ability – способность
# abroad – за границей
# access – доступ
# advantage – преимущество
# amateur – любитель, непрофессионал
# apparent – очевидный, явный
# to be essential – быть существенным
# to be worth – иметь ценность
# to change – менять, изменять
# communication – информация; коммуникация
# confirm – подтверждать
# contemporary – современный
# demand – требование
# experience – опыт
# experienced specialist – опытный специалист
# fashion – мода
# to get acquainted with – познакомиться
# to insist on – настаивать на чемлибо
# interpreter – переводчик
# mentality – склад ума
# negotiations – переговоры
# to notice – замечать
# opportunity – возможность
# to realize – понимать, осознавать
# to require – требовать
# to spend – тратить, расходовать
# stable – стойкий; устойчивый
# stylish – стильный, модный
# to sum up – суммировать; обобщать
# tolerance – терпимость; толерантность
# to travel – путешествовать
# to understand – понимать
# valuable – ценный
# vision – видение
# vulnerable – уязвимый, ранимый
# to waste time – зря тратить время'''.split("\n")
#
# string = list(map(lambda x: x.split(' – ')[::-1], string))
#
# for i in string:
#     print(*i, sep='-')

# import numpy
#
# def reset_array(arr: numpy.array) -> None:
#     for i in range(arr.size):
#         arr.put(i, 0)

# def radix_sort(arr: list[int, ...], base = 10) -> None:
#     max_digits = max(arr, key=lambda x: len(str(x)))
#     bins = numpy.array([numpy.array([0]*len(arr))]*base)
#     for i in range(max_digits):
#         for j in range(len(arr)):
#             bins.

# print(radix_sort([1, 2, 3]))
# bins = numpy.array([numpy.array([i for i in range(5)])]*7)
# print(bins[2][1])

# def six_angle_number():
#     num = 1
#     k = 1
#     while True:
#         yield num
#         num += 6 * k
#         k += 1
#
#
# gen = six_angle_number()
# print(type(gen))
# for i in range(10):
#     print(gen.__next__())

# import time
# import pyautogui
#
# time.sleep(4)
#
# for i in range(10000):
#     pyautogui.rightClick()
#     time.sleep(0.005)

# import turtle
#
# t = turtle.Pen()  # Создаём черепаху
# t.left(90)  # Поворачиваем черепаху вертикально вверх, как в задании
# t.speed(1000)  # Скорость повыше чтобы не ждать ответа ~100500 лет
# k = 6  # Коэффициент увеличения рисунка. Для корректного подсчёта должен быть 100,
# # но поначалу рекомендую ставить 1, чтобы посмотреть, адекватный ли рисунок выходит
#
# # Просто рисуем то, что сказано в задании
# t.begin_fill()  # Нам нужно закрасить фигуру
# for i in range(6):  # Тут надо выставить такое количество повторов, чтобы фигура рисовалась только один раз!!!
#                     # Чтобы она не обводила себя несколько раз, внимательно следите!
#     t.right(36)
#     t.forward(10 * k)
#     t.right(36)
# t.end_fill()
#
# #
#
# turtle.mainloop()

# import string
#
# def caesar(word, rot=1):
#     result = ""
#     for i in word:
#         if i in string.ascii_uppercase:
#             result += string.ascii_uppercase[(string.ascii_uppercase.index(i) + rot) % 26]
#         elif i in string.ascii_lowercase:
#             result += string.ascii_lowercase[(string.ascii_lowercase.index(i) + rot) % 26]
#         else:
#             result += i
#     return result
#
#
# print(caesar("flag_..._cHaneL_..._..._...", -1))

# import random
#
# flag = "<DELETED>"
#
# if __name__ == "__main__":
#     key = random.randint(1, 1024)
#     encrypted = ""
#     for i in flag:
#         encrypted += str(ord(i) ^ key) + " "
#     print(encrypted)

# nums = [51, 57, 52, 50, 10, 123, 123, 123, 10, 123, 123, 123, 10, 3, 60, 5, 10, 123, 123, 123, 10, 123, 123, 123]
# key = 85
#
# res = ''
#
# for i in nums:
#     res += chr(i ^ key)
#
# print(res)

# import keyboard
# import time
#
# time.sleep(5)  # Hello - it is for copy
#
# for i in range(10):
#     keyboard.press("ctrl+v, enter")
#     time.sleep(0.01)

# import turtle  # То чем будем рисовать
#
# t = turtle.Pen()  # создание ручки
# t.speed(10000)  # Чтобы рисовалось быстрее
# k = 100  # Увеличиваем масштаб фигуры.
# # ВСЕГДА в конце задачи поменять на k=100. По мере выполнения можно принять k=1-10, чтобы
# # проверить, корректно ли рисуется
# t.left(90)  # По условию черепаха смотрит вверх, а у нас по-умолчанию вправо
#
# # Переписываем код.
# # Важно все ПЕРЕМЕЩЕНИЯ умножать на k, а ПОВОРОТЫ не трогать
#
# # Чтобы посчитать точки внутри фигуры, её надо залить
# t.begin_fill()
# for i in range(3):  # Тут важно подобрать такое количество повторов,
#     # чтобы черепаха рисовала фигуру ровно один раз (не обводила). Для этого
#     # рекомендую поставить скорость на 3 и посмотреть, не обводит ли черепаха фигуру
#     # дважды. Если обводит - уменьшить количество повторов
#     t.forward(111 * k)
#     t.right(120)
# t.end_fill()
#
# # Далее начинаем считать точки внутри
# cnt = 0
# canvas = turtle.getcanvas()  # Считываем весь холст чтобы на нём смотреть точки
# for x in range(-400 * k, 400 * k, k):
#     for y in range(-400 * k, 400 * k, k):
#         tmp = canvas.find_overlapping(x, y, x, y)
#         # эта функция находит пересечения прямоугольника с координамами x0, y0, x1, y1 с фигурами
#         # на холсте. Если передать координты x, y, x, y - получится точка, тогда мы будем искать,
#         # пересекает ли точка какую-либо фигуру
#         if tmp == (5, ):  # Если в tmp записалось только 5, то точка пересекает только заливку
#             # вопросы почему именно 5 не принимаются, ответом является хуй знает, просто заливка
#             # это 5
#             cnt += 1
#
# print(cnt)
#
# turtle.mainloop()  # чтобы экран не гас

print("A B AxorB")

for i in range(2):
    for j in range(2):
        print(i, j, i^j)
