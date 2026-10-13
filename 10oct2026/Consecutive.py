a = [100, 4, 200, 1, 3, 2, 2]
lis = set()
lis.update(a)
a = sorted(list(lis))
print(a)
seq = 0
length =1
for cur in range(1, len(a)):
    pre = cur-1
    if a[cur] == a[pre]+1:
        length = length+1
    seq = max(length, seq)
print(seq)
