n = input()

sum = 0

for i in n:
    sum = sum + int(i) ** len(n)

if sum == int(n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")
