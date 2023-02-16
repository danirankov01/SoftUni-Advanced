n = int(input())
matrix = [[int(x) for x in input().split()] for i in range(n)]

while(True):
    commands = input().split()
    if(commands[0] == "END"): break

    command = commands[0]
    row, col, value = int(commands[1]), int(commands[2]), int(commands[3])

    if(0 <= row < len(matrix) and 0 <= col < len(matrix)):
        if(command == "Add"):
            matrix[row][col] += value

        elif(command == "Subtract"):
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

for row in range(n):
    for col in range(n):
        print(matrix[row][col], end=" ")
    print()