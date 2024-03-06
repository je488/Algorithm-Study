#BOJ_15652_1.py와 유사한 문제
#BOJ_15652_1.py와 달리 1 ~ N중에 M을 고르는 것이 아닌 입력으로 주어지는 N개의 수 중에 M개 고르기
#수열은 사전 순으로 증가하는 순서로 출력해야 하므로 N개의 수가 들어있는 a를 오름차순으로 정렬
#s는 어디서부터 수를 채울 수 있는지에 대한 범위의 시작 인덱스값
#중복 선택이 가능하므로 idx번째 숫자가 a[i]면 idx+1번째에 올 수 있는 숫자는 a[i] ~ a[n-1]
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = [0] * m
def go(idx, s):
    if idx == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        return
    for i in range(s, n):
        ans[idx] = a[i]
        go(idx+1, i)

go(0, 0)
