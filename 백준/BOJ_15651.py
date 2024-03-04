#BOJ_15649.py와 매우 유사한 문제로 차이점은 숫자를 중복해서 선택할 수 있음
#BOJ_15649.py와 달리 중복이 가능하므로 숫자의 사용 여부를 체크하는 check 리스트 불필요
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
a = [0] * m
def go(idx):
    if idx == m:
        sys.stdout.write(' '.join(map(str, a)) + '\n')
        return
    for i in range(1, n+1):
        a[idx] = i
        go(idx+1)

go(0)
