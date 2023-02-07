clothes = [int(x) for x in input().split()]
capacity = int(input())
saveCapacity = capacity

racks = 1

while clothes:
    current_item = clothes.pop()
    if saveCapacity - current_item >= 0:
        saveCapacity -= current_item
        
    else:
        racks += 1
        saveCapacity = capacity
        saveCapacity -= current_item

print(racks)