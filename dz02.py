a = []
for i in range(1, 1001, 2):
    a.append(i ** 3)
print(a)

b = []
total = 0
for num in a:
    i = num
    while num != 0:
        total += num % 10
        num = num // 10
    if total % 7 == 0:
        b.append(i)
    total = 0
print(sum(b))