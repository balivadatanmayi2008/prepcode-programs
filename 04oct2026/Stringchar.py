a = input()

letters = 0
digits = 0
special = 0

for i in a:
    n = ord(i)

    if (65 <= n <= 90) or (97 <= n <= 122):
        letters += 1
    elif 48 <= n <= 57:
        digits += 1
    else:
        special += 1

print("Letters:", letters)
print("Digits:", digits)
print("Special:", special)