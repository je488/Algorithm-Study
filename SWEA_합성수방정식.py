import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def iscn(s):
    for i in range(2, int(s**0.5)+1):
        if s % i == 0:
            return True
    return False
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    i = 4
    while True:
        if iscn(i) and iscn(i + n):
            print(f'#{tc} {i+n} {i}')
            break
        i += 1
