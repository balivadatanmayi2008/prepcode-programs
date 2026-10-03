r = int(input("Enter a number: "))
sum = 0
l = 1
while l < r:
    if r % l == 0:
        sum = sum + l
    l = l + 1
if sum == r:
    print("Perfect Number")
else:
    print("not a Perfect Number")