n = int(input())
stack = []

for i in range(n):
    line = input().split()

    if(line[0] == "1"):
        number = int(line[1])
        stack.append(number)

    elif(line[0] == "2"):
        if(len(stack) != 0):
            stack.pop()

    elif(line[0] == "3"):
        print(max(stack))

    elif(line[0] == "4"):
        print(min(stack))

print(*stack[::-1], sep=", ")