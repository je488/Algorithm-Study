#BOJ_15652_2.py와 유사한 문제
#BOJ_15652_2.py와 달리 1 ~ N중에 M을 고르는 것이 아닌 입력으로 주어지는 N개의 수 중에 M개 고르기
#수열은 사전 순으로 증가하는 순서로 출력해야 하므로 N개의 수가 들어있는 a를 오름차순으로 정렬
#cnt[i]는 a의 i번째 숫자를 사용한 횟수
#idx는 a에 들어있는 숫자의 인덱스, selected는 현재 선택한 숫자의 개수
#a의 idx번째 숫자는 1개 ~ (m-selected)개만큼 선택 가능
#idx >= n인 경우 m개를 고르지 못했는데 더 이상 선택할 수 있는 숫자가 없는 경우로 함수 종료
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
cnt = [0] * n
def go(idx, selected):
    if selected == m:
        for i in range(n):
            for j in range(cnt[i]):
                sys.stdout.write(str(a[i]) + ' ')
        sys.stdout.write('\n')
        return
    if idx >= n:
        return
    for i in range(m-selected, 0, -1):
        cnt[idx] = i
        go(idx+1, selected+i)
    cnt[idx] = 0
    go(idx+1, selected)

go(0, 0)
