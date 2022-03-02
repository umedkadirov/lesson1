m = 60
hour = m * 60
day = hour * 24
week = day * 7
time_series = [59, 3599, 36000, 86300, 450000, 500000]
for duration in time_series:
    if duration < m:
        print(duration, 'сек')
    elif duration < hour:
        print(duration // m, 'мин', duration % m, 'сек')
    elif duration < day:
        print(duration // hour, 'час', duration % hour // m, 'мин', duration % m, 'сек')
    elif duration < week:
        print(duration // day, 'ден', duration % day // hour, 'час', duration % hour // m, "мин", duration % m, 'сек')
    else:
        print(duration // week, "ден", duration % week // day, duration % day // hour, 'час',
              duration % hour // m, 'мин', duration % m, 'сек')
