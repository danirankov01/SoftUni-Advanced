def positiveOrNegative(*args):
    positive = list(filter(lambda x: x >= 0, *args))
    negative = list(filter(lambda x: x < 0, *args))

    print(sum(negative))
    print(sum(positive))

    if(sum(positive) > abs(sum(negative))):
        return "The positives are stronger than the negatives"

    else:
        return "The negatives are stronger than the positives"

numbers = [int(x) for x in input().split()]
print(positiveOrNegative(numbers))