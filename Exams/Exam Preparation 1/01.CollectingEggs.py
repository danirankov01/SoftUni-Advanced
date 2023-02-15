from collections import deque

eggs = deque([int(x) for x in input().split(", ")])
papers = [int(x) for x in input().split(", ")]

boxes = 0

while(eggs and papers):
    egg = eggs[0]
    paper = papers[-1]

    if(egg <= 0): 
        eggs.remove(egg)
        continue

    if(egg == 13):
        eggs.remove(egg)
        papers[0], papers[-1] = papers[-1], papers[0]
        continue

    eggs.popleft()
    papers.pop()
    
    if(egg + paper <= 50):
        boxes += 1

if(boxes != 0):
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if(eggs):
    print(f"Eggs left: ", end="")
    print(*eggs, sep=", ")

if(papers):
    print(f"Pieces of paper left: ", end="")
    print(*papers, sep=", ")