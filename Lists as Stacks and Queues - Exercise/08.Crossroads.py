from collections import deque

greenLight = int(input())
window = int(input())

saveGreen = greenLight
saveWindow = window

crash = False
windowStart = False
passedCars = 0


while(True):
    line = input()
    
    if(line == "END"): break

    if(line != "green"):
        if(not windowStart):
            car = deque(list(line))
            if(len(car) <= greenLight):
                greenLight -= len(car)
                passedCars += 1

            else:
                if(len(car) <= greenLight + window):
                    difference = len(car) - greenLight
                    greenLight = 0
                    window -= difference
                    windowStart = True
                    passedCars += 1

                else:
                    saveCar = car.copy()
                    for i in range(greenLight + window):
                        car.popleft()
                    
                    print("A crash happened!")
                    for i in range(len(saveCar)):
                        print(saveCar[i], end="")
                    print(f" was hit at {car[0]}.")
                    exit()


        else:
            greenLight = saveGreen
            window = saveWindow
            windowStart = False

    else:
        greenLight = saveGreen
        window = saveWindow

print("Everyone is safe.")
print(f"{passedCars} cars passed the crossroads.")