from collections import deque

foodPortions = [int(x) for x in input().split(", ")]
stamina = deque([int(x) for x in input().split(", ")])

peaksClimbed = []
mountains = {"Vihren": 80,
            "Kutelo": 90,
            "Banski Suhodol": 100, 
            "Polezhan": 60,
            "Kamenitza": 70
}

while(mountains and foodPortions and stamina):
    firstMountainValue = list(mountains.values())[0]
    firstMountain = list(mountains.keys())[0]
    
    currentFood = foodPortions.pop()
    currentStamina = stamina.popleft()

    if(currentFood + currentStamina >= firstMountainValue):
        peaksClimbed.append(firstMountain)
        del mountains[firstMountain]

if(len(peaksClimbed) == 5):
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")

else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if(peaksClimbed):
    print("Conquered peaks:")
    print(*peaksClimbed,sep='\n')