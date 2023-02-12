n = int(input())

matrix = [[int(x) for x in input().split(", ")] for i in range(n)]

print("Primaty diagonal: ", end="")
sumFirst = 0

for row in range(len(matrix)):
    if(row + 1 < len(matrix)):
        print(matrix[row][row], end=", ")
        sumFirst += matrix[row][row]
    else:
        print(matrix[row][row], end=". ")
        sumFirst += matrix[row][row]

print(f"Sum: {sumFirst}")

print("Secondrary diagonal: ", end="")
sumSecond = 0
index = len(matrix) - 1

for row in range(len(matrix)):
    if(row + 1 < len(matrix)):
        print(matrix[row][index], end=", ")
        sumSecond += matrix[row][index]
        index -= 1
    else:
        print(matrix[row][index], end=". ")
        sumSecond += matrix[row][index]

print(f"Sum: {sumSecond}")