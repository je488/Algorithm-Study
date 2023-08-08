#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXSVc1TqEAYDFAQT(문제링크)
#robots의 키는 로봇의 이름, 값은 로봇의 위치와 시간(특정 시간이 흘렀을 때 로봇의 위치)
#dist는 로봇에서 버튼까지의 거리(버튼이 로봇의 현재위치보다 왼쪽에 있을 수도 있으므로 절대값 구하기)
#robot_sec는 로봇이 이동가능한 시간(1초에 1미터 이동가능하므로 로봇이 이동가능한 거리와 같음)
#dist가 robot_sec보다 작거나 같으면 로봇이 버튼까지 이미 이동 -> 추가로 이동할 필요 없음
#따라서 버튼만 누르면 되므로 ans += 1
#dist가 robot_sec보다 크면 추가로 이동해야 하므로 dist-robot_sec+1 값 더하기(+1은 버튼 누르는 시간)
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    li = list(input().split())
    n = int(li[0])
    robots = {'O' : [1, 0], 'B' : [1, 0]}
    ans = 0
    for i in range(1, n*2, 2):
        name = li[i]
        button = int(li[i+1])
        dist = abs(button - robots[name][0])
        robot_sec = ans - robots[name][1]
        if dist <= robot_sec:
            ans += 1
        else:
            ans += dist - robot_sec + 1
        robots[name] = [button, ans]
    print(f'#{tc} {ans}')
