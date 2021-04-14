# 1以上n以下の各自然数の約数の個数を保持する配列を返す
def num_divisors_table(n):
    table = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            table[j] += 1

    return table
