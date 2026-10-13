l={1,3,2,4,100,2,200}
s=set()
s.update(1)
l=sorted(list(s))
count=1
print(l)
length=0
for cur in range(l,len(l)):
    prev=cur-1
    if l[prev]+l==l[cur]:
     count=count+1
    else:
        count=1
    length=max(count,length)   
print(length)         