n = int(input())

vip = set()
regular = set()

for i in range(n):
    code = input()

    if(48 <= ord(code[0]) <= 57):
        vip.add(code)
    else:
        regular.add(code)

while(True):
    code = input()
    if(code == "END"): break

    if(code in vip):
        vip.remove(code)

    if(code in regular):
        regular.remove(code)

print(len(vip) + len(regular))

vip = tuple(sorted(vip))
regular = tuple(sorted(regular))

for i in vip:
    print(i)

for i in regular:
    print(i)