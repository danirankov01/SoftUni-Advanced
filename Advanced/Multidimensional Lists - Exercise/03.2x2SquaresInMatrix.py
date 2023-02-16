rows, cols = [int(x) for x in input().split()]
matrix = []

for i in range(rows):
    matrix.append([x for x in input().split()])

counter = 0

for row in range(rows - 1):
    for col in range(cols - 1):

        topLeft = matrix[row][col]
        topRight = matrix[row][col + 1]
        bottomLeft = matrix[row + 1][col]
        bottomRight = matrix[row + 1][col + 1]

        if(topLeft == topRight == bottomLeft == bottomRight):
            counter += 1

print(counter)