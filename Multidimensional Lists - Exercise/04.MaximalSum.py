# rows, cols = [int(x) for x in input().split()]
# matrix = [[int(x) for x in input().split()] for i in range(rows)]

# best = {
#     'bestSum': float('-inf'),
#     'row': 0,
#     'col': 0
# }

# bestSum = 0

# if(rows >= 3 and cols >= 3):
#     for rol in range(rows - 2):
#         for col in range(cols - 2):
#             sum = 0

#             for rolCol in range(rol, rol + 3):
#                 sum += sum(matrix[rolCol][col:col+3])