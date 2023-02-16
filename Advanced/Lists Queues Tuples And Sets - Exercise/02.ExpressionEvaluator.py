from collections import deque

queue = deque(input().split())
numbers = []

while(len(queue) > 1):
    for i in range(len(queue)):
        current = queue.popleft()
        
        if(current == "+"):
            new = 0
            for i in numbers:
                new += i
            queue.appendleft(new)
            numbers = []
            break
        elif(current == "-"):
            new = numbers[0] * 2
            for i in numbers:
                new -= i
            queue.appendleft(new)
            numbers = []
            break
        elif(current == "*"):
            new = 1
            for i in numbers:
                new *= i
            queue.appendleft(new)
            numbers = []
            break
        elif(current == "/"):
            if(numbers[0] != 0):
                new = numbers[0] ** 2
            else:
                new = 0
                
            for i in numbers:
                new = int(new / i)
            queue.appendleft(new)
            numbers = []
            break

        else:
            numbers.append(int(current))

print(new)