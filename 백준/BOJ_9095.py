import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def go(s, goal):
    if s > goal:
        return 0
    if s == goal:
        return 1
    now = 0
    for i in range(1, 4):
        now += go(s + i, goal)
    return now
T = int(input())
for _ in range(T):
    n = int(input())
    print(go(0, n))