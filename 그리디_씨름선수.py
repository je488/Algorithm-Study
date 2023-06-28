import sys
sys.stdin = open("input.txt", "r")
n = int(input())
info = []
for _ in range(n):
    height, weight = map(int, input().split())
    info.append((height, weight))
info.sort(reverse = True)
cnt = 0
max_value = 0
for height, weight in info:
    if weight > max_value:
        cnt += 1
        max_value = weight
print(cnt)
