from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque([x for x in input().split()])
totalHoney = 0

while(bees and nectar):
    if(nectar[-1] - bees[0] >= 0):

        symbol = symbols.popleft()
        currentBee = bees.popleft()
        currentNectar = nectar.pop()

        if(symbol == "+"): totalHoney += abs(currentBee + currentNectar)
        elif(symbol == "-"): totalHoney += abs(currentBee - currentNectar)
        elif(symbol == "*"): totalHoney += abs(currentBee * currentNectar)
        elif(symbol == "/"): totalHoney += abs(currentBee / currentNectar)

    else:
        nectar.pop()

print(f"Total honey made: {totalHoney}")
if(bees):
    print("Bees left: ", end="")
    print(*bees, sep=", ")

if(nectar):
    print("Nectar left: ", end="")
    print(*nectar, sep=", ")