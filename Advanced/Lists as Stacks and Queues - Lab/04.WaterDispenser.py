from collections import deque

waterInDispenser = int(input())
peoples = deque()

while(True):
    names = input()
    if(names == "Start"): break
    peoples.append(names)

while(True):
    commands = input().split()

    if(commands[0] == "End"): break

    if(commands[0] == "refill"):
        liters = int(commands[1])
        waterInDispenser += liters

    else:
        wantedWater = int(commands[0])
        currentPerson = peoples.popleft()
        if(waterInDispenser >= wantedWater):
            print(f"{currentPerson} got water")
            waterInDispenser -= wantedWater

        else:
            print(f"{currentPerson} must wait")

print(f"{waterInDispenser} liters left")