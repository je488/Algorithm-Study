import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
s = input()
for i in range(0, len(s), 10):
    print(s[i:i+10])
