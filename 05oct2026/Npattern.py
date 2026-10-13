n=int(input())
for row in range (0,n):
    for col in range(0,n): 
        if col==0 or col==n-1 or row+col==n-1:
           print("* ",end=" ")
        else:
           print("  ",end=" ")
    print ()   
