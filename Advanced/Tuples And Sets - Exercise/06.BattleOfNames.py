n = int(input())
even = set()
odd = set()

for i in range(1, n + 1):
    name = input()
    sum = 0

    for j in name:
        sum += (ord(j))

    sum = int(sum / i)
    if(sum % 2 == 0):
        even.add(int())
    else:
        odd.add(sum)

if(sum(even) == sum(odd)):
    print(even.union(odd), sep=", ")

elif(sum(even) > sum(odd)):
    print(even.symmetric_difference(odd), sep=", ")

else:
    even = set((even))
    odd = set((odd))
    result = [even - odd]
    result.extend(odd - even)
    print(*result, sep=", ")


# seta = {1, 2, 6, 7, 8}

# seta = set((seta))
# setb = set((1, 2, 3, 4, 9))
# lista = list(seta - setb)
# lista.extend(setb - seta)
# print(lista)