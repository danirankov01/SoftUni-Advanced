from collections import deque

foodQuantity = int(input())
queue = deque(int(x) for x in input().split())

print(max(queue))

while(foodQuantity != 0 or queue):
    order = queue[0]
    if(order <= foodQuantity):
        foodQuantity -= order
        queue.popleft()

        if(not queue):
            print("Orders complete")
            break

    else:
        print("Orders left:", *queue)
        break