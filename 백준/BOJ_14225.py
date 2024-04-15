import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
c = [False] * n * 100000
def go(i, sum):
    if i == n:
        c[sum] = True
        return
    go(i+1, sum+s[i])
    go(i+1, sum)
go(0, 0)
i = 1
while True:
    if c[i] == False:
        break
    i += 1
print(i)