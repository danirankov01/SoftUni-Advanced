from collections import deque

kids = deque(input().split())
toss = int(input())

while(len(kids) > 1):
    for i in range(1, toss + 1):
        if(i % toss == 0):
            print(f"Removed {kids.popleft()}")
            break

        kids.append(kids.popleft())

print(f"Last is {kids[0]}")