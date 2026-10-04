n = int(input())

s = 0

for i in str(n):
    value = int(i) ** 3
    print(i, "** 3 =", value)
    s = s + value

print("Sum =", s)

if s == n:
    print("Armstrong")
else:
    print("Not Armstrong")