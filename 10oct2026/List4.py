n=int(input())
l=[int(input()) for i in range(n)]
ans=["even" if val%2==0 else "odd"for val in l]
print(l)
print(ans)