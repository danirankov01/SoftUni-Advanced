n = int(input())
peoples = {}

for i in range(n):
    line = input().split()

    name = line[0]
    grade = float(line[1])
    
    if(name not in peoples):
        peoples[name] = [grade]

    else:
        peoples[name].append(grade)

for k, v in peoples.items():
    print(f"{k} ->", end=" ")
    for values in peoples[k]:
        print(f"{values:.2f}", end=" ")
    print(f"(avg: {sum(peoples[k]) / len(peoples[k]):.2f})")