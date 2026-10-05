n=int(input())
for row in range(0,n):
    for col in range(0,n):
        if row ==col:
            print("* ",end =" ")
        elif row+col==n-1:
            print("* ",end =" ")    
        else:
            print(" ",end =" ")    
    print()    