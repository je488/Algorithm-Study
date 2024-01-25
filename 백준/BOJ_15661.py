#BOJ_14889_1.py와 달리 두 팀의 인원이 N // 2명이어야 한다는 조건이 없음
#따라서 index가 n이 되어 팀 배정이 끝나면 각 팀의 인원수가 0보다 큰지만 체크
#각 팀의 인원수가 모두 0보다 크면 두 팀의 능력치 차이를 리턴하고 그렇지 않으면 -1 리턴
#능력치의 차이값을 리턴받으면 이전에 구한 정답(ans)과 비교하여 값이 작으면 ans값 바꿔주기
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def go(index, first, second):
    if index == n:
        if len(first) == 0:
            return -1
        if len(second) == 0:
            return -1
        t1 = 0
        t2 = 0
        for p1 in first:
            for p2 in first:
                if p1 == p2:
                    continue
                t1 += s[p1][p2]
        for p1 in second:
            for p2 in second:
                if p1 == p2:
                    continue
                t2 += s[p1][p2]
        diff = abs(t1 - t2)
        return diff
    ans = -1
    t1 = go(index + 1, first + [index], second)
    if ans == -1 or (t1 != -1 and ans > t1):
        ans = t1
    t2 = go(index + 1, first, second + [index])
    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2
    return ans

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
print(go(0, [], []))
