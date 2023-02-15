presents = int(input())
n = int(input())

niceKids = 0
noPresents = False
kidsHappy = False
end = False

matrix = [[x for x in input().split()] for i in range(n)]
movement = {
    'left': [-1, 0], 'right': [1, 0], 'up': [0, -1], 'down': [0, 1]
}

for i in range(n):
    for j in range(n):
        if(matrix[i][j] == "S"):
            santa = [i, j]
        if(matrix[i][j] == "V"):
            niceKids += 1

saveNiceKids = niceKids

while(True):
    commands = input()
    if(commands == "Christmas morning"): 
        end = True
        break
    
    rowMovement, colMovement = movement[commands]

    saveRow, saveCol = santa

    if(0 <= saveRow + colMovement < len(matrix) and 0 <= saveCol + rowMovement < len(matrix)):
        santa[0] += colMovement
        santa[1] += rowMovement
        matrix[saveRow][saveCol] = '-'

        if(matrix[santa[0]][santa[1]] == "V"):
            presents -= 1
            niceKids -= 1

            if(presents == 0 and niceKids > 0):
                print("Santa ran out of presents!")
                noPresents = True
                matrix[santa[0]][santa[1]] = "S"
                break

            matrix[santa[0]][santa[1]] = "S"

        elif(matrix[santa[0]][santa[1]] == "C"):
            for i in movement:
                r = santa[0] + movement[i][1]
                c = santa[1] + movement[i][0]
                move = matrix[r][c]

                if(move == "V"):
                    presents -= 1
                    niceKids -= 1
                elif(move == "X"):
                    presents -= 1

                matrix[r][c] = "-"

                if(presents == 0):
                    if(niceKids > 0):
                        print("Santa ran out of presents!")
                        noPresents = True
                        break
                    else:
                        kidsHappy = True
                        break

                matrix[r][c] = "-"

        matrix[santa[0]][santa[1]] = "S"

        if(presents == 0 and niceKids > 0):
            noPresents = True
            break
        if(presents == 0 and niceKids == 0):
            kidsHappy = True
            break

if(end):
    for row in range(n):
        for col in range(n):
            print(matrix[row][col], end=" ")
        print()

    print(f"Good job, Santa! {saveNiceKids} happy nice kid/s.")

if(noPresents):
    for row in range(n):
        for col in range(n):
            print(matrix[row][col], end=" ")
        print()
    
    print(f"No presents for {niceKids} nice kid/s.")