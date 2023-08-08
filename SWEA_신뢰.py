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
