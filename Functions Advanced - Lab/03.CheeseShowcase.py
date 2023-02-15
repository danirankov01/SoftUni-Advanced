def sorting_cheeses(**kwargs):
    cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""
    for c, q in cheeses:
        result += c + "\n"
        sortedCheeses = sorted(q, reverse=True)
        result += "\n".join([str(x) for x in sortedCheeses]) + "\n"

    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135], 
        Camembert=[100, 100, 105, 500, 430], 
        Mozzarella=[50, 125],
    )
)
