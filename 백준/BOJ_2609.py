import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)
a, b = map(int, input().split())
gcd = GCD(a, b)
lcm = a * b // gcd
print(gcd)
print(lcm)