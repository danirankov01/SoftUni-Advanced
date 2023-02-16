from collections import deque

def fill_the_box(*args):
    queue = deque(args)
    sizeOfTheBox = 1
    for i in range(3):
        currentElement = queue.popleft()
        sizeOfTheBox *= currentElement

    while(len(queue) > 1 and queue[0] != "Finish"):
        currentElement = queue.popleft()

        if(sizeOfTheBox >= currentElement):
            sizeOfTheBox -= currentElement

        else:
            difference = currentElement - sizeOfTheBox
            rest = 0
            for i in range(len(queue) - 1):
                rest += queue[i]
            output = difference + rest
            return f"No more free space! You have {output} more cubes."

    return f"There is free space in the box. You could put {sizeOfTheBox} more cubes."


print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))