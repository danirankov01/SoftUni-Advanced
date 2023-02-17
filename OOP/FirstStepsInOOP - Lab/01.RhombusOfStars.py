def printRombus(n, i):
    print(' ' * (n - i), end="")
    for j in range(1, i + 1):
        print('*', end=" ")
    print()


n = int(input())

for i in range(1, n + 1):
    printRombus(n, i)

for j in range(n - 1, 0, -1):
    printRombus(n, j)


# print('4' * 4)
