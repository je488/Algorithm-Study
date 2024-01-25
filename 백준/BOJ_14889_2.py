#BOJ_14889_1.py는 모든 경우를 다 해보는 것이므로 브루트 포스
#브루트 포스에 특정 조건을 추가하여 중간에 호출을 중단시키면 백트래킹
#특정 팀의 인원이 N // 2명을 넘는 경우는 불가능한 경우로 함수 호출 종료 -> 백트래킹
#BOJ_14889_1.py보다 시간 단축
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def go(index, first, second):
    if index == n:
        if len(first) != n // 2:
            return -1
        if len(second) != n // 2:
            return -1
        t1 = 0
        t2 = 0
        for i in range(n // 2):
            for j in range(n // 2):
                if i == j:
                    continue
                t1 += s[first[i]][first[j]]
                t2 += s[second[i]][second[j]]
        diff = abs(t1 - t2)
        return diff
    if len(first) > n // 2:
        return -1
    if len(second) > n // 2:
        return -1
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
