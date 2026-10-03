a = int(input("Enter a: "))
n = int(input("Enter n: "))

sum = 0
i = a

while i <= n:
    sum = sum + i
    i = i + 1

print("Sum of values from", a, "to", n, "=", sum) 