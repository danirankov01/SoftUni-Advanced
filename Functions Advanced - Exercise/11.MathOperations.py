from collections import deque

def math_operations(*args, a, s, d, m):
    numbers = deque()
    for t in args:
        numbers.append(t)
    
    result = {'a': a, 's': s, 'd': d, 'm': m}
    index = 0

    for i in range(len(numbers)):
        if(index == 0):
            result['a'] += numbers[i]
        elif(index == 1):
            result['s'] -= numbers[i]
        elif(index == 2):
            if(numbers[i] != 0):
                result['d'] /= numbers[i]
        elif(index == 3):
            result['m'] *= numbers[i]

        index += 1

        if(index == 4):
            index = 0

    sortedResult = sorted(result.items(), key=lambda x: (-x[1], x[0]))
    output = []
    for i in range(len(sortedResult)):
        output.append(f"{sortedResult[i][0]}: {sortedResult[i][1]:.1f}")

    return '\n'.join(output)


print(math_operations(6.0, a=0, s=0, d=5, m=0))