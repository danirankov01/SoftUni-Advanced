from collections import deque

cupsCapacity = deque([int(x) for x in input().split()])
bottlesCapacity = [int(x) for x in input().split()]

wasted = 0

while(cupsCapacity and bottlesCapacity):
    currentBottle = bottlesCapacity.pop()

    if(currentBottle - cupsCapacity[0] >= 0):
        wasted += currentBottle - cupsCapacity[0]
        cupsCapacity.popleft()

    else:
        cupsCapacity[0] -= currentBottle

if(not cupsCapacity):
    print("Bottles:", *bottlesCapacity)

if(not bottlesCapacity):
    print("Cups:", *cupsCapacity)

print(f"Wasted litters of water: {wasted}")