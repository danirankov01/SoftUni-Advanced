n = int(input())
cars = set()

for i in range(n):
    line = input().split(", ")

    if(line[0] == "IN"):
        cars.add(line[1])
    else:
        cars.remove(line[1])

if(not cars):
    print("Parking Lot is Empty")

else:
    for i in cars:
        print(i)