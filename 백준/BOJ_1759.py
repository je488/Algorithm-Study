import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def check(password):
    ja = 0
    mo = 0
    for p in password:
        if p in "aeiou":
            mo += 1
        else:
            ja += 1
    return mo >= 1 and ja >= 2

def go(n, alpha, password, i):
    if len(password) == n:
        if check(password):
            print(password)
        return
    if i == len(alpha):
        return
    go(n, alpha, password + alpha[i], i + 1)
    go(n, alpha, password, i + 1)

l, c = map(int, input().split())
alpha = input().split()
alpha.sort()
go(l, alpha, "", 0)