#BOJ_15650_2.py와 유사한 문제
#BOJ_15650_2.py와 달리 1 ~ N중에 M을 고르는 것이 아닌 입력으로 주어지는 N개의 수 중에 M개 고르기
#수열이 오름차순이 되어야 하므로 N개의 수가 들어있는 a를 오름차순으로 정렬
#go는 a[0] ~ a[n-1]까지 각각의 숫자를 선택할지 말지 결정하는 함수
#idx는 a에 들어있는 숫자의 인덱스, cnt는 선택한 숫자의 개수
#idx >= n인 경우 m개를 고르지 못했는데 더 이상 선택할 수 있는 숫자가 없는 경우로 함수 종료
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = [0] * m
def go(idx, cnt):
    if cnt == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        return
    if idx >= n:
        return
    ans[cnt] = a[idx]
    go(idx+1, cnt+1)
    ans[cnt] = 0
    go(idx+1, cnt)

go(0, 0)
