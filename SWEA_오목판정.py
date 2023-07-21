#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXaSUPYqPYMDFASQ(문제링크)
#ifFive함수를 이용하여 돌이 가로, 세로, 대각선 중 한 방향으로 5개 이상 연속하는지 체크
#dr, dc는 가로, 세로, 오른쪽대각선, 왼쪽대각선을 탐색하기 위한 행과 열의 인덱스 증가치
#li에서 'o'가 발견되면 개수 세기 시작(발견된 순간 돌은 한개가 되므로 cnt는 1부터 시작)
#r과 c는 li의 행, 열 인덱스로 dr과 dc를 이용하여 가로, 세로, 오른쪽대각선, 왼쪽대각선 탐색
#r과 c가 0이상 n미만으로 li 안에 위치해야 하며 돌이 있으면 cnt를 증가시키고 한 방향으로 계속 이동
#돌이 어떤 방향으로든 5개 이상 연속되면 YES를 출력해야하므로 5개만 되면 YES 리턴(반복 종료)
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def isFive(li):
    dr = [0, 1, 1, 1]
    dc = [1, 0, 1, -1]
    for i in range(n):
        for j in range(n):
            if li[i][j] == 'o':
                for k in range(4):
                    cnt = 1
                    r = i + dr[k]
                    c = j + dc[k]
                    while 0 <= r < n and 0 <= c < n and li[r][c] == 'o':
                        cnt += 1
                        r += dr[k]
                        c += dc[k]
                        if cnt == 5:
                            return 'YES'
    return 'NO'
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    li = [input().rstrip() for _ in range(n)]
    print(f'#{tc} {isFive(li)}')
