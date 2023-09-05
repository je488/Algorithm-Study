#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWS2dSgKA8MDFAVT(문제링크)
#cnt는 박수를 치고있는 사람의 수, res는 고용해야 하는 사람의 수
#i는 info의 인덱스 및 info[i]명이 박수를 치기위해 필요한 최소 사람의 수
#cnt가 i보다 크거나 같으면 info[i]명이 박수를 치기 위해 필요한 사람의 수를 만족 -> info[i] 누적
#cnt가 i보다 작으면 사람을 고용해야 하므로 res에 부족한 사람 수(i - cnt) 누적
#사람을 고용하면 info[i]명도 박수를 칠 수 있으므로 cnt에 (i - cnt)와 info[i] 더하기
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T + 1):
    info = input().rstrip()
    cnt = 0
    res = 0
    for i in range(len(info)):
        if cnt >= i:
            cnt += int(info[i])
        else:
            res += (i - cnt)
            cnt += (int(info[i]) + i - cnt)
    print(f'#{tc} {res}')
