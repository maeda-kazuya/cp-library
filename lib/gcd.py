from functools import reduce

# 最大公約数
def gcd(a, b):
    # 大きい方を被除数、小さい方を除数とする
    dividend = max(a, b)
    divider = min(a, b)

    if divider == 0:
        return dividend

    # 最大公約数を見つけるまで繰り返す
    while dividend % divider != 0:
        # 除算を行い、その除数を次回の被除数、剰余を次回の除数として処理を繰り返す
        r = dividend % divider
        dividend = divider
        divider = r

    # 一方がもう一方を割り切れた時点で、その除数を最大公約数とみなせる
    return divider

# 最小公倍数
def lcm(a, b):
    return (a * b) // gcd(a, b)

A = [2, 3, 4]
LCM = reduce(lcm, A)

# 12
print(LCM)

