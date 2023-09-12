import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m, k = map(int, input().split())
li = list(map(int, input().split()))
li.sort(reverse=True)
res, cnt = 0, 0
cnt += m // (k+1) * k
cnt += m % (k+1)
res += cnt * li[0]
res += (m - cnt) * li[1]
print(res)
