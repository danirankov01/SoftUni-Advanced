firstSequence = set([int(x) for x in input().split()])
secondSequence = set([int(x) for x in input().split()])
n = int(input())

for i in range(n):
    command = input().split()
    numbers = []

    if(command[0] + command[1] == "AddFirst"):
        for i in range(len(command) - 2):
            firstSequence.add(int(command[i + 2]))

    elif(command[0] + command[1] == "AddSecond"):
        for i in range(len(command) - 2):
            secondSequence.add(int(command[i + 2]))

    elif(command[0] + command[1] == "RemoveFirst"):
        for i in range(len(command) - 2):
            if(int(command[i + 2]) in firstSequence):
                firstSequence.remove(int(command[i + 2]))

    elif(command[0] + command[1] == "RemoveSecond"):
        for i in range(len(command) - 2):
            if(int(command[i + 2]) in secondSequence):
                secondSequence.remove(int(command[i + 2]))

    elif(command[0] + command[1] == "CheckSubset"):
        if(firstSequence.issubset(secondSequence) or secondSequence.issubset(firstSequence)):
            print(True)
        else:
            print(False)

print(*firstSequence, sep=", ")
print(*secondSequence, sep=", ")