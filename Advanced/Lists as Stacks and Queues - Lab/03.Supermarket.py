from collections import deque

peoples = deque()

while(True):
    name = input()

    if(name == "End"): 
        print(f"{len(peoples)} people remaining.")
        break

    if(name != "Paid"):
        peoples.append(name)

    else:
        for i in range(len(peoples)):
            print(peoples[i])
        peoples.clear()