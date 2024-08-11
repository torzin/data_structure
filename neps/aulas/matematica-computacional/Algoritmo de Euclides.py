# Maior divisor comum
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


a, b = map(int, input().split())

print(f"Maior divisor comum de {a} e {b}: {gcd(a, b)}")


# MMC (mínimo múltiplo comum)
def lcm(a, b):
    ans = a * b
    ans = ans / gcd(a, b)

    return ans


a, b = map(int, input().split())

print(f"Mínimo múltiplo comum de {a} e {b}: {lcm(a, b)}")
