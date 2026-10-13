n=int(input())
l=[int(input()) for i in range(n)]
ans=["pass" if val>=40 else"fail" for val in l]
print (ans)