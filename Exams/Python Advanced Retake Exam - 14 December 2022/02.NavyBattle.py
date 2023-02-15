n = int(input())
battlefield = [[x for x in input()] for i in range(n)]

cruisers = 3
hits = 3

for i in range(n):
    for j in range(n):
        if(battlefield[i][j] == "S"):
            row, col = i, j

movement = {'up': [0, -1], 'down': [0, 1], 'left': [-1, 0], 'right': [1, 0]}

while(True):
    command = input()
    saveRow = row
    saveCol = col

    rowMovement, colMovement = movement[command]
    row += colMovement
    col += rowMovement

    if(battlefield[row][col] == "*"):
        battlefield[saveRow][saveCol] = "-"
        battlefield[row][col] = "S"
        hits -= 1

        if(hits == 0):
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
            break

    elif(battlefield[row][col] == "C"):
        battlefield[saveRow][saveCol] = "-"
        battlefield[row][col] = "S"
        cruisers -= 1

        if(cruisers == 0):
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

    else:
        battlefield[saveRow][saveCol] = "-"
        battlefield[row][col] = "S"

for i in range(n):
    for j in range(n):
        print(battlefield[i][j], end="")
    print()