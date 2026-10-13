tanmayi= dict()
s = input("enter your name")
for ch in s:
    if ch not in tanmayi:
        tanmayi[ch] = 1
    else:
        tanmayi[ch] = tanmayi[ch] + 1
print(tanmayi)
