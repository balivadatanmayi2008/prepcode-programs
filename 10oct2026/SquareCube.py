n=int(input())
l=[int(input()) for i in range(n)]
ans=[val**2 if val %2==0 else val**3 for val in l]
print(ans)