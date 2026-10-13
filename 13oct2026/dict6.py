n=int(input())
val=1
for row in range(n):
    for col in range(n):
        if col <=row:
            print(val,end=" ")
            val= val+1
    print()      