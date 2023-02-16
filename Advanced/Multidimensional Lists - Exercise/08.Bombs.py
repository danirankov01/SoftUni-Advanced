rows = int(input())
matrix = [[int(x) for x in input().split()] for i in range(rows)]
incides = [int(x) for x in input().replace(" ", ",").split(",")]

movement = {
    'up': [0, -1], 'down': [0, 1], 'left': [-1, 0], 'right': [1, 0],
        'top left': [-1, -1], 'top right': [1, -1],
        'bottom left': [-1, 1], 'bottom right': [1, 1]
}

for i in range(0, len(incides), 2):
    row, col = incides[i], incides[i + 1]
    currentBomb = matrix[row][col]
    saveRow = row
    saveCol = col

    for j in movement:
        rowMovement, colMovement = movement[j]
        row += colMovement
        col += rowMovement

        if(0 <= row < len(matrix) and 0 <= col < len(matrix)):
            if(matrix[row][col] > 0):
                matrix[row][col] -= currentBomb

        row = saveRow
        col = saveCol

    matrix[row][col] = 0

alive = 0
sum = 0

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if(matrix[i][j] > 0):
            alive += 1
            sum += matrix[i][j]

print(f"Alive: {alive}")
print(f"Sum: {sum}")

for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j], end=" ")
    print()