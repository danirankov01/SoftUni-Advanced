n = int(input())
commands = input().split()
matrix = [[x for x in input().split()] for i in range(n)]

collectedCoal = False


movement = {
    'up': [0, -1], 'down': [0, 1], 'left': [-1, 0], 'right': [1, 0]
}

coalToCollect = 0

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if(matrix[i][j] == "s"):
            row, col = i, j
        elif(matrix[i][j] == "c"):
            coalToCollect += 1

for i in commands:
    rowMovement, colMovement = movement[i]

    saveRow = row
    saveCol = col

    if(0 <= row + colMovement < len(matrix) and 0 <= col + rowMovement < len(matrix)):
        row += colMovement
        col += rowMovement

        if(matrix[row][col] == "e"):
            print(f"Game over! ({row}, {col})")
            exit()

        elif(matrix[row][col] == "c"):
            coalToCollect -= 1
            if(coalToCollect == 0):
                print(f"You collected all coal! ({row}, {col})")
                collectedCoal = True
                break

        matrix[saveRow][saveCol] = "*"
        matrix[row][col] = "s"

if(not collectedCoal):
    print(f"{coalToCollect} pieces of coal left.")
    print(f"({row}, {col})")