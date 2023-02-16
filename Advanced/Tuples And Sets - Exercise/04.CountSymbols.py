text = input()
times = {}

for i in range(len(text)):
    if(text[i] not in times):
        times[text[i]] = 1
    else:
        times[text[i]] += 1

# dict(sorted(times.items(), key=lambda time: time[0]))

keys = list(times.keys())
keys.sort()
sortedTimes = {i: times[i] for i in keys}

for k, v in sortedTimes.items():
    print(f"{k}: {v} time/s")