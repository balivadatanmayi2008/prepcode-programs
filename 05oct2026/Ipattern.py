n = int(input())
for row in range(0, n):
    for col in range(0, n):
        if row == 0 or row == n - 1 or col == n // 2:
            print("* ", end=" ")
        else:
            print("   ", end="")
    print()
