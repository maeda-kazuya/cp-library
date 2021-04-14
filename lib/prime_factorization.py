# Return a list of the prime factors for a natural number bigger than 1
def trial_division(n):
    if n < 2:
        return []

    prime_factors = []

    for i in range(2, int(n**0.5)+1):
        # nがi（の累乗）で割り切れるかを調べる
        while n % i == 0:
            # nがiで割り切れる場合、iを素因数としてリストに追加する
            prime_factors.append(i)
            # nをiで割った商で更新しておく
            n //= i
    # nの平方根より大きい素因数が存在する場合
    if n > 1:
        prime_factors.append(n)

    return prime_factors

n = int(input())
print(trial_division(n))