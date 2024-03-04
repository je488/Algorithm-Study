#BOJ_15649.py와 매우 유사한 문제로 차이점은 수열이 오름차순이어야 함
#s는 어디서부터 수를 채울 수 있는지에 대한 범위의 시작값
#수열이 오름차순이 되어야 하므로 idx번째의 숫자가 i면 idx+1번째 숫자는 i+1부터 가능
#따라서 idx번째의 숫자를 i로 결정한 뒤에 go(idx+1, i+1) 호출
#s를 이용하여 다음 자리 숫자를 결정할 때 s ~ n의 범위에서 결정하므로 숫자는 중복될 수 없음
#따라서 숫자의 사용 여부를 체크하는 check 리스트 불필요
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
        go(idx+1, i+1)

go(0, 1)
