rows = int(input())

for i in range(rows):
    if(i == 0):
        result = [int(x) for x in input().split(", ")]
    else:
        result.extend([int(x) for x in input().split(", ")])