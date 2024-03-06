#BOJ_15649.py와 유사한 문제
#BOJ_15649.py와 달리 1 ~ N중에 M을 고르는 것이 아닌 입력으로 주어지는 N개의 수 중에 M개 고르기
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
check = [0] * n
ans = [0] * m
def go(idx):
    if idx == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        return
    for i in range(n):
        if check[i] == 1:
            continue
        check[i] = 1
        ans[idx] = a[i]
        go(idx+1)
        check[i] = 0

go(0)
