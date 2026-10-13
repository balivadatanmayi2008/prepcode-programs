tanmayi= dict()
s=input("enter your name")
i=0
for ch in s:
    if ch not in tanmayi:
        tanmayi[ch]=[i]
    else:
        tanmayi[ch].append(i)
    i=i+1
print(tanmayi)           