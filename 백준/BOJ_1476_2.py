import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
E, S, M = map(int, input().split())
E -= 1
S -= 1
M -= 1
year = 0
while True:
    if year % 15 == E and year % 28 == S and year % 19 == M:
        print(year + 1)
        break
    year += 1