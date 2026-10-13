n=int(input())
l=[int(input()) for i in range(n)]
ans=[val if val>0 else 0 for val in l]
print(l)
print(ans)