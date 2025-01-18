#求两个整数的最大公约数

def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)

def gcd_iterative(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

print(gcd_iterative(24,36))

