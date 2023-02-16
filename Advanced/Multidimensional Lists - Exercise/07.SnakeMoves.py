rows, cols = [int(x) for x in input().split()]
snake = input()
index = 0

for row in range(rows):
    result = []

    for col in range(cols):
        if(index == len(snake)):
            index = 0

        if(row % 2 == 0):
            result.append(snake[index])
        else:
            result.insert(0, snake[index])
        index += 1
    
    print(*result, sep="")