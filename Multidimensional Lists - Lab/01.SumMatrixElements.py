matrix = []

rows, cols = [int(x) for x in input().split(", ")]
sumOfMatrix = 0

for i in range(rows):
    numbers = input().split(", ")
    inner = []
    for j in range(cols):
        inner.append(int(numbers[j]))
        sumOfMatrix += int(numbers[j])
    matrix.append(inner)

print(sumOfMatrix)
print(matrix)