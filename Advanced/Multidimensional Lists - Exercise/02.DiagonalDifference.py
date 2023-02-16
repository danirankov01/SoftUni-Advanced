n = int(input())
matrix = [[int(x) for x in input().split()] for i in range(n)]

diagonals = {
    'primary': [],
    'secondary': []
    }

for i in range(len(matrix)):
    diagonals['primary'].append(matrix[i][i])
    diagonals['secondary'].append(matrix[i][len(matrix) - i - 1])

print(f"{abs(sum(diagonals['primary']) - sum(diagonals['secondary']))}")
