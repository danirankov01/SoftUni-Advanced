line = input().split("|")
result = []

for i in range(len(line) - 1, -1, -1):
    numbers = [x for x in line[i].split()]
    result.extend(numbers)

print(' '.join(result))