numbers = [int(x) for x in input().split()]
stack = []

for i in range(len(numbers)):
    stack.append(numbers.pop())

print(*stack)