input_intervals = int(input())
points = []
while input_intervals > 0:
    input_intervals -= 1
    interval_start, interval_end = input().split()
    interval_start = int(interval_start)
    interval_end = int(interval_end)
    points.append([interval_start, -1])  # начало делаем -1 для нужной сортировки
    points.append([interval_end, 1])

points.sort()
#print(points)

maxvac = 0
maxvacnum = 0
maxvactime = 0
count = 0
for p in points:
    if p[1] < 0:  #начало
        count += 1
        if count > maxvac:   #всё обнуляем
            maxvac = count
            maxvacnum = 1
            maxstart = p[0]
            maxvactime = 0
        elif count == maxvac:
            maxvacnum += 1   #обновляем количество лучших
            maxstart = p[0]
    else:
        if count == maxvac:  # конец интервала с лучшим пока набором
            maxvactime += p[0] - maxstart + 1
        count -=1

print(maxvacnum, maxvactime)