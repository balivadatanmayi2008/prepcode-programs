l = [2, 7, 1, 19, 18, 3]
n = len(l)
total = 0
for i in range(1, n + 1):
    if n % i == 0:
        total += l[i - 1] ** 2
print(total)
