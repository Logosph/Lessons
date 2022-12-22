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
from pyautogui import press, typewrite
from time import sleep

sleep(6)

for i in range(498):
    typewrite("spam")
    press("enter")
    sleep(0.05)

# print("".join(
#     random
#     .choices(
#         string.ascii_letters +
#         string.digits +
#         string.punctuation,
#         k=10
#     )
# ))


