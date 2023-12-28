import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
x, y = map(int, input().split())
res = 0
for i in range(x-1):
    res += date[i]
res += y
print(week[res % 7])