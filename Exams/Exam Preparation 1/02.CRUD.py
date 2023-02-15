matrix = [[x for x in input().split()] for i in range(6)]

pos = input()
position = [int(pos[1]), int(pos[4])]

movement = {
    'up': [0, -1], 'down': [0, 1], 'left': [-1, 0], 'right': [1, 0]    
}

while(True):
    line = input().split(", ")
    
    command = line[0]
    if(command == "Stop"): break

    direction = line[1]
    
    rowMovement, colMovement = movement[direction]
    nextRow = position[0] + colMovement
    nextCol = position[1] + rowMovement
    
    if(command == "Create"):
        value = line[2]

        if(matrix[nextRow][nextCol] == "."):
            matrix[nextRow][nextCol] = value

    elif(command == "Update"):
        value = line[2]
        
        if(matrix[nextRow][nextCol] != "."):
            matrix[nextRow][nextCol] = value

    elif(command == "Delete"):
        matrix[nextRow][nextCol] = "."

    elif(command == "Read"):
        if(matrix[nextRow][nextCol] != "."):

            if(matrix[nextRow][nextCol].isdigit()):
                print(int(matrix[nextRow][nextCol]))
            else:
                print(matrix[nextRow][nextCol])

    position = [nextRow, nextCol]

for row in range(6):
    for col in range(6):
        print(matrix[row][col], end=" ")
    print()