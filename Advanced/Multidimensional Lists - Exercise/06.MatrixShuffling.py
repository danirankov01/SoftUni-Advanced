rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for i in range(rows)]

while(True):
    command = input().split()
    if(command[0] == "END"): break

    if(command[0] == "swap" and len(command) == 5):
        row1 = int(command[1])
        col1 = int(command[2])

        row2 = int(command[3])
        col2 = int(command[4])

        if(row1 >= 0 and col1 >= 0 and row2 >= 0 and col2 >= 0 \
            and row1 < cols and col1 < cols and row2 < cols and col2 < cols):

            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            
            for row in range(rows):
                for col in range(cols):
                    print(matrix[row][col], end=" ")
                print()

        else:
            print("Invalid input!")

    else:
        print("Invalid input!")