n, m = [int(x) for x in input().split()]
matrix = [[x for x in input()] for i in range(n)]
commmands = list(input())

movements = {
    'U': [0, -1], 'D': [0, 1], 'L': [-1, 0], 'R': [1, 0]
}

spreadUp = [0, -1]
spreadDown = [0, 1]
spreadLeft = [-1, 0]
spreadRight = [1, 0]

won = False
dead = False

for i in range(n):
    for j in range(m):
        if(matrix[i][j] == "P"):
            row, col = i, j
            break

for i in commmands:
    rowMovement, colMovement = movements[i]

    saveRow, saveCol = row, col

    for r in range(n):
        for c in range(m):
            if(matrix[r][c] == "B"):
                bunnyRow, bunnyCol = r, c
                if(0 <= bunnyRow + spreadUp[1] < n and 0 <= bunnyCol + spreadUp[0] < m):
                    matrix[bunnyRow + spreadUp[1]][bunnyCol + spreadUp[0]] = 'b'

                if(0 <= bunnyRow + spreadDown[1] < n and 0 <= bunnyCol + spreadDown[0] < m):
                    matrix[bunnyRow + spreadDown[1]][bunnyCol + spreadDown[0]] = 'b'

                if(0 <= bunnyRow + spreadLeft[1] < n and 0 <= bunnyCol + spreadLeft[0] < m):
                    matrix[bunnyRow + spreadLeft[1]][bunnyCol + spreadLeft[0]] = 'b'

                if(0 <= bunnyRow + spreadRight[1] < n and 0 <= bunnyCol + spreadRight[0] < m):
                    matrix[bunnyRow + spreadRight[1]][bunnyCol + spreadRight[0]] = 'b'

    for r in range(n):
        for c in range(m):
            if(matrix[r][c] == 'b'):
                matrix[r][c] = 'B'

    if(0 <= row + colMovement < n and 0 <= col + rowMovement < m):
        row += colMovement
        col += rowMovement

        if(matrix[row][col] == "B"):
            dead = True
            break

        matrix[row][col] = "P"
        matrix[saveRow][saveCol] = "."

    else:        
        matrix[row][col] = "."
        won = True
        break


for i in range(n):
    for j in range(m):
        print(matrix[i][j], end="")
    print()


if(won): 
    print(f"won: {row} {col}")

if(dead):
    print(f"dead: {row} {col}")

# 5 6
# ......
# .....P
# ...B..
# ......
# ......
# UUDDDR
