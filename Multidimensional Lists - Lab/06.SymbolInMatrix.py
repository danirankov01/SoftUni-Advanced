rows = int(input())
matrix = []

for i in range(rows):
    cols = [x for x in input()]
    matrix.append(cols)

search = input()
finded = False

for i in range(rows):
    for j in range(rows):
        if(matrix[i][j] == search):
            finded = True
            print(f"({i}, {j})")
            exit()

print(f"{search} does not occur in the matrix")   