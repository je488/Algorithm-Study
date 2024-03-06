#BOJ_15650_1.py와 유사한 문제
#BOJ_15650_1.py와 달리 1 ~ N중에 M을 고르는 것이 아닌 입력으로 주어지는 N개의 수 중에 M개 고르기
#수열은 사전 순으로 증가하는 순서로 출력해야 하므로 N개의 수가 들어있는 a를 오름차순으로 정렬
#s는 어디서부터 수를 채울 수 있는지에 대한 범위의 시작 인덱스값
#s를 이용하여 다음 자리 숫자를 결정할 때 a[s] ~ s[n-1]의 범위에서 결정
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
        go(idx+1, i+1)

go(0, 0)
