import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
cnt = int(input())
divisor = list(map(int, input().split()))
print(min(divisor) * max(divisor))