numbers = list(map(int, input().split()))
n = numbers[0]
m = numbers[1]

nSet = set()
mSet = set()

for i in range(n + m):
    number = int(input())
    if(i + 1 <= n):
        nSet.add(number)
    else:
        mSet.add(number)

nList = list(nSet)
mList = list(mSet)

if(len(nList) >= len(mList)):
    for i in range(len(nList)):
        if(nList[i] in mList):
            print(nList[i])

else:
    for i in range(len(mList)):
        if(mSet[i] in mList):
            print(mList[i])