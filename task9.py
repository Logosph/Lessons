def six_angle_number(maximum):
    num = 1
    for i in range(1, maximum + 1):
        yield num
        num += 6 * i


gen = six_angle_number(5)
for j in gen:
    print(j)
