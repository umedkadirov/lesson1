for num in range(1, 101):
    if num % 10 in [0, 5, 6, 7, 8, 9] or (10 < num < 20):
        print(num, 'процентов')
    elif num % 10 == 1:
        print(num, 'процент')
    else:
        print(num, 'процента')