def prime_numbers(numbers):
    prime = []
    for current in numbers:
        if current > 1:
            for i in range(2, current):
                if current % i == 0:
                    break
            else:
                prime.append(current)

    return prime


def get_primes(iterable):
    prime = prime_numbers(iterable)
    for num in prime:
        yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
