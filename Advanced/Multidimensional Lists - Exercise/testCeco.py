n, m = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for i in range(n)]

biggestSum = float("-inf")
currentSum = 0
destination = ""

sequence = []
bestSequence = []

count = 0
isValid = True

#horizontal

if(m >= 4):
    for row in range(n):
        difference = m - 4
        for col in range(difference + 1):
            sequence = []
            currentSum = sum(matrix[row][col:col + 4])
            sequence.extend(matrix[row][col:col + 4])

            if(currentSum > biggestSum):
                biggestSum = currentSum
                destination = "horizontal"
                bestSequence = sequence.copy()

else:
    isValid = False


#vertical
if(n >= 4):
    for col in range(m):
        difference = n - 4
        for row in range(difference + 1):
            sequence = []
            currentSum = 0
            for ver in range(4):
                currentSum += matrix[ver + row][col]
                sequence.append(matrix[ver + row][col])

            if(currentSum > biggestSum):
                biggestSum = currentSum
                destination = "vertical"
                bestSequence = sequence.copy()

else:
    isValid = False


#diagonal

if(n >= 4 and m >= 4):

#first diagonal

    for col in range(n - 3):
        for row in range(m - 3):
            sequence = []
            currentSum = 0

            for i in range(4):
                currentSum += matrix[col + i][row + i]
                sequence.append(matrix[col + i][row + i])

            if(currentSum > biggestSum):
                biggestSum = currentSum
                destination = "diagonal"
                bestSequence = sequence.copy()


#reverse diagonal

    for col in range(n - 3):
        for row in range(m - 3):

            sequence = []
            currentSum = 0

            for i in range(4):
                currentSum += matrix[col + i][m - 1 - row - i]
                sequence.append(matrix[col + i][m - 1 - row - i])

            if(currentSum > biggestSum):
                biggestSum = currentSum
                destination = "reverse diagonal"
                bestSequence = sequence.copy()

else:
    isValid = False

if(not isValid):
    print("You should enter at least 4x4 matrix.")

else:
    print(f"Biggest 4 sequence of numbers is on the {destination}.\nThe sequence is {bestSequence} and it's sum is {biggestSum}.")

# for i in range(n):
#     for j in range(m):
#         print(matrix[i][j], end=" ")
#     print()

# 1 2 3 1 8 9 5
# 4 5 6 8 8 9 5
# 7 8 9 5 8 9 5
# 6 8 1 3 8 9 5
# 8 2 3 6 1 3 5

# 1 2 3 1 8 9 5
# 4 5 6 8 8 9 5
# 7 8 9 5 8 9 5
# 6 8 1 3 8 9 5
# 8 2 3 6 1 3 5
# 6 3 1 8 9 1 4

# 1 2 3 7 8
# 5 7 1 9 3
# 4 1 2 9 0
# 6 4 2 1 7
# 9 4 2 7 3
# 1 8 5 3 2


#diagonal

# 1 2 3 4
# 6 2 5 9
# 9 3 7 8
# 4 2 4 6


# 1 2 3 4
# 7 8 3 9
# 1 0 4 6
# 4 5 7 1
# 5 6 8 3


#10x10

# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 6 7 8 10 3
# 1 2 3 4 5 6 7 10 9 7
# 1 2 3 4 5 6 10 8 9 8
# 1 2 3 4 5 6 7 8 9 5
# 1 2 3 4 5 6 7 8 9 1
# 1 2 3 4 5 6 7 8 9 3
# 1 2 3 4 5 6 7 8 9 9
# 1 2 3 4 5 6 7 8 9 0
# 1 2 3 4 5 6 7 8 9 2