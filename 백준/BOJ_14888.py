import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def calc(a, index, cur, plus, minus, mul, div):
    global max_res, min_res
    if index == len(a):
        max_res = max(cur, max_res)
        min_res = min(cur, min_res)
        return
    if plus > 0:
        calc(a, index+1, cur+a[index], plus-1, minus, mul, div)
    if minus > 0:
        calc(a, index+1, cur-a[index], plus, minus-1, mul, div)
    if mul > 0:
        calc(a, index+1, cur*a[index], plus, minus, mul-1, div)
    if div > 0:
        if cur >= 0:
            calc(a, index+1, cur//a[index], plus, minus, mul, div-1)
        else:
            calc(a, index+1, -(-cur//a[index]), plus, minus, mul, div+1)

n = int(input())
a = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
max_res = -int(1e9)
min_res = int(1e9)
calc(a, 1, a[0], plus, minus, mul, div)
print(max_res)
print(min_res)