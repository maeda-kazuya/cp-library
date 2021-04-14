'''
a / b = a * pow(b, -1) (mod p)
note: pow(b, -1) is gyakugen in mod p
'''

mod = 10**9+7

# xの逆元を返す
def modinv(x, mod):
    return pow(x, mod-2, mod)

# Get a / b in normal way
ans = a / b

# Get a / b in mod p
ans = a * modinv(b, mod)
