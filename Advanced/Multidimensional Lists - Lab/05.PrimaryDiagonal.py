rows = int(input())
matrix = []

for i in range(rows):
    cols = [int(x) for x in input().split()]
    matrix.append(cols)

sum = 0
for i in range(rows):
    sum += matrix[i][i]