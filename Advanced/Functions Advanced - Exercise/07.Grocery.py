def grocery_store(**kwargs):
    sortedGrocery = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    output = []

    for i in range(len(sortedGrocery)):
        output.append(f"{sortedGrocery[i][0]}: {sortedGrocery[i][1]}")

    return '\n'.join(output)

print(grocery_store(
    pasta=2,
    bread=2,
    eggs=20,
    carrot=1,
))
