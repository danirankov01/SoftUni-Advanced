from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milk = deque([int(x) for x in input().split(", ")])

milkshakes = 0

while(chocolates and milk):
    if(chocolates[-1] <= 0):
        chocolates.pop()
        if(not chocolates): break

    if(milk[0] <= 0):
        milk.popleft()
        if(not milk): break


    if(chocolates[-1] == milk[0]):
        milkshakes += 1
        chocolates.pop()
        milk.popleft()
        if(milkshakes == 5): break

    else:
        removed = milk.popleft()
        milk.append(removed)
        chocolates[-1] -= 5


if(milkshakes >= 5):
    print("Great! You made all the chocolate milkshakes needed!")

else:
    print("Not enough milkshakes.")

if(chocolates):
    print(f"Chocolate: ", end="")
    print(*chocolates, sep=", ")

else:
    print("Chocolate: empty")

if(milk):
    print(f"Milk: ", end="")
    print(*milk, sep=", ")

else:
    print("Milk: empty")