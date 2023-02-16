n = int(input())
longestIntersection = float("-inf")
numbers = []

for i in range(n):
    interceptions = input().split("-")
    firstNumbers = interceptions[0]
    secondNumbers = interceptions[1]

    splitted = firstNumbers.split(",")
    firstStart = int(splitted[0])
    firstEnd = int(splitted[1])

    splitted = secondNumbers.split(",")
    secondStart = int(splitted[0])
    secondEnd = int(splitted[1])

    firstMax = max(firstStart, secondStart)
    secondMin = min(firstEnd, secondEnd)

    counter = 0

    if(secondMin - firstMax + 1 > longestIntersection):
        longestIntersection = secondMin - firstMax + 1
        numbers = []

        for i in range(firstMax, secondMin + 1):
            numbers.append(i)

print(f"Longest intersection is {numbers} with length {longestIntersection}")
