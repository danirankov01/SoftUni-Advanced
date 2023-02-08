numbers = [float(x) for x in input().split()]
occurences = {}

for i in numbers:
    if(i not in occurences):
        occurences[i] = 1
    else:
        occurences[i] += 1

for k, v in occurences.items():
    print(f"{k} - {v} times")