rows = int(input())
matrix = []
for i in range(rows):
    cols = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix.append(cols)

print(matrix)