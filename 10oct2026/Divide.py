n=int(input())
l=[int(input()) for i in range(n)]
ans=[val for val in l if val%3==0 and val%5!=0]
print (ans)