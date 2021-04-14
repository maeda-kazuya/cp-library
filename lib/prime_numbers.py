# n以下の素数を返す
def prime_numbers(n):
    target = {}
    primes = []

    for i in range(2, n+1):
        # target.append(i)
        target[i] = False


    while True:
        prime = target[0]
        primes.append(prime)
        del target[0]

        for i in range(len(target)):
            if target[i]

    # for i in range(n**0.5+1):
    #     target[i]


