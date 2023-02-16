rows, cols = [int(x) for x in input().split()]
matrix = []

for i in range(97, 97 + rows):
    for j in range(97, 97 + cols):
        print(f"{chr(i)}{chr(i + j - 97)}{chr(i)}", end=" ")
    print()