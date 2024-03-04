#BOJ_15649.py에 BOJ_15650.py와 BOJ_15651.py의 조건을 추가한 문제
#숫자를 중복해서 선택할 수 있으므로 idx번째의 숫자가 i면 idx+1번째에 올 수 있는 수는 i ~ n
#따라서 idx번째의 숫자를 i로 결정한 뒤에 go(idx+1, i) 호출
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
a = [0] * m
def go(idx, s):
    if idx == m:
        sys.stdout.write(' '.join(map(str, a)) + '\n')
        return
    for i in range(s, n+1):
        a[idx] = i
        go(idx+1, i)

go(0, 1)
