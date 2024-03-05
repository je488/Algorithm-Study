#수열이 오름차순이므로 순서(BOJ_15650_1.py)가 아닌 선택 방법으로도 문제를 풀 수 있음
#go는 1 ~ n까지 각각의 숫자를 선택할지 말지 결정하는 함수
#idx는 숫자, cnt는 선택한 수의 개수
#선택한 수의 개수가 m개가 되면 수열 출력
#idx > n인 경우 m개를 고르지 못했는데 더 이상 선택할 수 있는 숫자가 없는 경우로 함수 종료
#숫자를 선택한 경우 idx와 cnt가 1씩 증가, 숫자를 선택하지 않은 경우 idx만 1 증가
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
a = [0] * m
def go(idx, cnt):
    if cnt == m:
        sys.stdout.write(' '.join(map(str, a)) + '\n')
        return
    if idx > n:
        return
    a[cnt] = idx
    go(idx+1, cnt+1)
    a[cnt] = 0
    go(idx+1, cnt)

go(1, 0)
