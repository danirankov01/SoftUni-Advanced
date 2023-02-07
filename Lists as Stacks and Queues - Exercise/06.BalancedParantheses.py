from collections import deque

parantheses = deque(input())
balanced = False
while(parantheses):
    first = parantheses.popleft()
    last = parantheses.pop()

    if(first == "(" and last == ")"):
        balanced = True
    elif(first == "[" and last == "]"):
        balanced = True
    elif(first == "{" and last == "}"):
        balanced = True

    else:
        balanced = False

if(balanced):
    print("YES")
else:
    print("NO")