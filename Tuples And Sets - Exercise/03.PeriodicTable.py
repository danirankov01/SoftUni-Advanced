n = int(input())
elements = set()

for i in range(n):
    element = input().split()
    for i in range(len(element)):
        elements.add(element[i])

for i in elements:
    print(i)