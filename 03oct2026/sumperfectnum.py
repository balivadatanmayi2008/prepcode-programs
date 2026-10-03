n = int(input("Enter a number: "))

sum = 0
i = 1

while i < n:
    if n % i == 0:
        print(i)
        sum = sum + i
    i = i + 1

print("Sum of factors =", sum)

if sum == n:
    print("The given number is a Perfect Number")
else:
    print("The given number is not a Perfect Number")