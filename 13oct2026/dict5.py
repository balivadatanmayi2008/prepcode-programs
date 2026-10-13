n=int(input())
for row in  range(n):
    val =1
    for col in range(n):
        if col <= row:
            print(val,end=" ")
            val=val+1
    print()            