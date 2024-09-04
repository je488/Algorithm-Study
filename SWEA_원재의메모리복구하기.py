#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV19AcoKI9sCFAZN(문제링크)
#cur은 현재 상태를 나타내는 변수, memory는 원래 상태의 메모리 값, ans는 수정 횟수
#memory의 비트를 하나씩 탐색하면서 cur과 비교해서 값이 다르면 cur의 값을 바꿔주고 ans값 1 증가
#메모리 값을 바꿀 때마다 현재 위치부터 끝까지 같은 값으로 덮어씌워짐
#따라서 현재 비트와 다음 비트가 같은 값이 되므로 리스트 대신 cur만 사용해도 메모리 값 비교 가능
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    memory = input().rstrip()
    cur = '0'
    ans = 0
    for m in memory:
        if m != cur:
            cur = m
            ans += 1
    print(f'#{tc} {ans}')
