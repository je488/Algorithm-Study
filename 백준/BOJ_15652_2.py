#수열이 비내림차순이므로 순서(BOJ_15652_1.py)가 아닌 선택 방법으로도 문제를 풀 수 있음
#중복 선택이 가능하므로 숫자를 선택하는 경우 몇 개를 선택했는지 cnt에 기록
#cnt[i]는 숫자 i를 사용한 횟수
#idx는 숫자, selected는 현재 선택한 숫자의 개수
#숫자 idx는 1개 ~ (m-selected) 개만큼 선택 가능, 수열은 사전 순으로 출력해야 함
#따라서 수의 개수가 가장 많은 m-selected부터 가장 적은 1까지 감소하는 방식으로 구현
#ex) 1112와 1123중 1112가 사전 순으로 더 앞에 위치
#숫자를 선택한 경우 idx는 1 증가하고 selected는 i만큼 증가
#숫자를 선택하지 않은 경우 idx만 1 증가
#선택한 숫자의 개수가 m개가 되면 cnt를 이용하여 수열 출력
#idx > n인 경우 m개를 고르지 못했는데 더 이상 선택할 수 있는 숫자가 없는 경우로 함수 종료
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
cnt = [0] * (n+1)
def go(idx, selected):
    if selected == m:
        for i in range(1, n+1):
            for j in range(1, cnt[i]+1):
                sys.stdout.write(str(i) + ' ')
        sys.stdout.write('\n')
        return
    if idx > n:
        return
    for i in range(m-selected, 0, -1):
        cnt[idx] = i
        go(idx+1, selected+i)
    cnt[idx] = 0
    go(idx+1, selected)

go(1, 0)
