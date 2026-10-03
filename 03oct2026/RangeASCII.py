name = input("Enter your name: ")

sum = 0

for i in name:
    print(i, "=", ord(i))
    sum = sum + ord(i)

print("Sum of ASCII values =", sum)

if sum % 2 == 0:
    print("Even")
else:
    print("Odd")