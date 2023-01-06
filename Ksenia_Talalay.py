# Number 14

# Системы счисления в петухоне
# 1) Из N в 10 систему:
# a = int("<число в N-ной системе счисления>", N) -> будет число в 10 СС

# number_bin = "1001010010100111101010100"
# number_dec = int(number_bin, 2)
# print(number_dec)

# number_sevens = "1036251421"
# number_dec = int(number_sevens, 7)
# print(number_dec)

# 2) Из 10 в N-ую
# а) Из 10 в 2-ую:
#   bin(N) -> "0b10010101010010"

# number_dec = 1234
# number_bin = bin(number_dec)[2:]
#
# print(number_bin)

# б) Из 10 в 8-ую
#   oct(N) -> "0o12054013501460"  octagonal

# number_dec = 1234
# number_oct = oct(number_dec)[2:]
#
# print(number_oct)

# в) Из 10 в 16-ую
#   hex(N) -> "0x1AB76D5F"

# number_dec = 1234
# number_hex = hex(number_dec)[2:]
#
# print(number_hex)

# Из любой другой в 10

# def perevod_v_Nuy(number, N):
#     res = ""
#     while number != 0:
#         res += str(number % N)
#         number //= N
#
#     return res[::-1]
#
# def perevod_v_7(N):
#     res = ""
#     while N != 0:
#         res += str(N % 7)
#         N //= 7
#
#     return res[::-1]
#
# print(perevod_v_7(49))  # 100

# Операнды арифметического выражения записаны в системах счисления с основаниями 9 и 11:
# 88x4y_9 + 7x44y_11
# В записи чисел переменными x и y обозначены допустимые в данных системах счисления неизвестные
# цифры. Определите значения x и y, при которых значение данного арифметического выражения будет
# наименьшим и кратно 61. Для найденных значений x и y вычислите частное от деления значения
# арифметического выражения на 61 и укажите его в ответе в десятичной системе счисления.
# Основание системы счисления в ответе указывать не нужно.

# X и Y - максимум 8, минимум 0

'''for x in range(9):
    for y in range(9):
        temp = int("88" + str(x) + "4" + str(y), 9) + int("7" + str(x) + "44" + str(y), 11)
        if temp % 61 == 0:
            print(temp, temp // 61)

print("-"*50)

for x in "012345678":
    for y in "012345678":
        temp = int("88" + x + "4" + y, 9) + int("7" + x + "44" + y, 11)
        if temp % 61 == 0:
            print(temp, temp // 61)'''

'''for x in '0123456789abc':
    for y in '0123456789abc':
        a= int('8'+x+'78'+y,13) + int('79'+ x+y+'7',18)
        if a %9==0:
            print(a//9)'''
#
#
# for x in '0123456789a':
#     for y in '0123456789a':
#         a = int(x + '341' + y, 11) + int('56' + x + '1' + y, 19)
#         if a % 305 == 0:
#             print(a // 305)
#             break

# Исполнитель Черепаха действует на плоскости с декартовой системой координат.
# В начальный момент Черепаха находится в начале координат, её голова направлена
# вдоль положительного направления оси ординат, хвост опущен. При опущенном хвосте
# Черепаха оставляет на поле след в виде линии. В каждый конкретный момент известно
# положение исполнителя и направление его движения. У исполнителя существует две команды:
# Вперёд n (где n — целое число), вызывающая передвижение Черепахи на n единиц в том направлении,
# куда указывает её голова, и Направо m (где m — целое число), вызывающая изменение направления движения на
# m градусов по часовой стрелке. Запись
#
# Повтори k [Команда1 Команда2 … КомандаS]
#
# означает, что последовательность из S команд повторится k раз. Черепахе был дан для исполнения следующий алгоритм:
#
# Повтори 4 [Вперёд 8 Направо 90 Вперёд 8 Направо 90]
#
# Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией,
# заданной данным алгоритмом. Точки на линии учитывать не следует.

'''import turtle

# Сетап ручки
pen = turtle.Pen()
pen.left(90)
pen.speed(1000)
k = 100

# Переписываем условие
pen.begin_fill()
for i in range(2):  # Важно выставить столько повторений, чтобы фигура нарисовала сама себя ровно 1 раз!
    pen.forward(8 * k)
    pen.right(90)
    pen.forward(8 * k)
    pen.right(90)
pen.end_fill()

cnt = 0
canvas = turtle.getcanvas()  # canvas - холст
for x in range(-300 * k, 300 * k, k):
    for y in range(-300 * k, 300 * k, k):
        s = canvas.find_overlapping(x, y, x, y)
        if s == (5, ):
            cnt += 1

print(cnt)
turtle.mainloop()'''

'''import turtle
pen=turtle.Pen()
pen.left(90)
pen.speed(10)
k=100

pen.begin_fill()
for i in range(3):
    pen.forward(10 * k)
    pen.right(120)
pen.end_fill()

cnt = 0
canvas = turtle.getcanvas()
for x in range(-300 * k, 300 * k, k):
    for y in range(-300*k,300*k,k):
        s=canvas.find_overlapping(x,y,x,y)
        if s== (5,):
            cnt+=1
print(cnt)


turtle.mainloop()'''

'''import turtle
pen=turtle.Pen()
pen.left(90)
pen.speed(100)
k=100

pen.begin_fill()
for i in range(3):
    pen.forward(9*k)
    pen.right(120)
pen.end_fill()

cnt=0
canvas = turtle.getcanvas()
for x in range(-300*k,300*k,k):
    for y in range(-300*k,300*k,k):
        s=canvas.find_overlapping(x,y,x,y)
        if s==(5,):
            cnt+=1
print(cnt)
turtle.mainloop()'''

# import turtle
# pen=turtle.Pen()
# pen.left(90)
# pen.speed(100)
# k=100
#
# pen.begin_fill()
# for i in range(3):
#     pen.forward(111*k)
#     pen.right(120)
# pen.end_fill()
#
# cnt=0
# canvas=turtle.getcanvas()
# for x in range(-300*k,300*k,k):
#     for y in range(-300 * k, 300 * k, k):
#         s=canvas.find_overlapping (x,y,x,y)
#         if s == (5,):
#             cnt += 1
# print(cnt)
# turtle.mainloop()

# import re
#
# f = open("24_demo (4).txt")
# text = f.read()
# f.close()
#
# xs = re.findall("X+", text)
# print(len(max(xs, key=len)))

# f = open("inf_22_10_20_24 (1).txt")
#
# cnt = 0
# for i in f:
#     if i.count("E") > i.count('A'):
#         cnt += 1
#
# print(cnt)
# f.close()

# import re
# f = open("24 (2).txt")
# text = f.read()
# f.close()
#
# finded = re.findall("A[A-Z]?", text)
# arr = [0] * 26
# for i in finded:
#     arr[ord(i[1]) - ord("A")] += 1
# print(chr(arr.index(max(arr)) + ord("A")))

# f = open("24 (2).txt")
#
# string = f.readline()
#
# for i in f:
#     if string.count("G") > i.count("G"):
#         string = i

# print(max(string, key=string.count))

# arr = [0] * 26
# for i in string[:-1:]:
#     arr[ord(i) - ord("A")] += 1
#
# print(arr)
# print(chr(19 + ord("A")))
