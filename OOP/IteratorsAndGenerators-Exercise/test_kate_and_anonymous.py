# from collections import deque
#
# n = int(input())
#
# maze = [
#     input() for i in range(n)
# ]
#
#
# def find_exit(maze, start_row, start_col):
#     """
#     This function uses breadth-first search to find the shortest path to the exit.
#     """
#     rows = len(maze)
#     cols = len(maze[0])
#     visited = [[False for _ in range(cols)] for _ in range(rows)]
#     queue = deque([(start_row, start_col, 0)])
#
#     while queue:
#         row, col, distance = queue.popleft()
#
#         if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
#             # Found an exit!
#             return f"Kate got out in {distance + 1} moves"
#
#         for drow, dcol in ((-1, 0), (1, 0), (0, -1), (0, 1)):
#             new_row = row + drow
#             new_col = col + dcol
#
#             if (
#                     0 <= new_row < rows and
#                     0 <= new_col < cols and
#                     maze[new_row][new_col] == " " and
#                     not visited[new_row][new_col]
#             ):
#                 visited[new_row][new_col] = True
#                 queue.append((new_row, new_col, distance + 1))
#
#     return "Kate cannot get out"
#
#
# # Find Kate's starting position
# for i, row in enumerate(maze):
#     if "k" in row:
#         k_row = i
#         k_col = row.index("k")
#         break
#
# print(find_exit(maze, k_row, k_col))


def merge(start_index, end_index):
    global arr
    arr_len = len(arr)
    start_index = max(start_index, 0)
    end_index = min(end_index, arr_len - 1)
    merged_str = ''.join(arr[start_index:end_index+1])
    arr = arr[:start_index] + [merged_str] + arr[end_index+1:]


def divide(index, partitions):
    global arr
    substr_len = len(arr[index]) // partitions
    last_substr_len = substr_len + len(arr[index]) % partitions
    substrings = [arr[index][i:i+substr_len] for i in range(0, len(arr[index])-last_substr_len+1, substr_len)]
    substrings[-1] = arr[index][-last_substr_len:]
    arr = arr[:index] + substrings + arr[index+1:]


arr = input().split()

while True:
    command = input()
    if command == '3:1':
        print(' '.join(arr))
        break
    else:
        tokens = command.split()
        if tokens[0] == 'merge':
            start_index, end_index = int(tokens[1]), int(tokens[2])
            merge(start_index, end_index)
        elif tokens[0] == 'divide':
            index, partitions = int(tokens[1]), int(tokens[2])
            divide(index, partitions)