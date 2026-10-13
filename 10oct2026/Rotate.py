a=[10,20,30,40,50,60]
k=2
n=len(a)
s=a[n-k: :]
f=a[0:n-k: ]
print(s+f)
