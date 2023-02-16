math = list(input())
result = []

for i in range(len(math)):
    if(math[i] == "("):
        result.append(i)

    elif(math[i] == ")"):
        removed = result.pop()
        print("".join(math[removed: i + 1]))