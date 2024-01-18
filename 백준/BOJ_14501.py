#상담에 필요한 시간과 버는 돈에 따라 상담을 하는 것이 좋을 수도, 좋지 않을 수도 있음
#따라서 모든 방법 시도 -> 각 날짜마다 상담을 하는 경우와 하지 않는 경우의 수익 구하기
#상담 여부에 따라 날짜(day)와 수입(s)이 달라지므로 재귀 함수의 인자로 추가
#go(day, s)에서 s는 day-1일까지의 수익
#상담을 하는 경우 상담을 끝낸 다음날(day + t[day])로 이동하고 수익(s + p[day])도 증가
#상담을 하지 않는 경우 바로 다음날(day + 1)로 이동하고 수익(s)은 증가하지 않음
#문제에서는 1일부터 N일까지 상담 후 N+1일에 퇴사
#코드에서는 인덱스가 0부터 시작하므로 0일부터 N-1일까지 상담 후 N일에 퇴사하는 것으로 가정
#day == n인 경우 상담을 끝낸 다음날이 퇴사일이므로 정답을 찾은 경우에 해당
#따라서 이전에 구한 정답(ans)보다 크면 ans값 바꿔주기 
#day > n인 경우 상담을 끝낸 다음날이 퇴사일 이후이므로 상담이 불가능한 경우 -> return
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
t = [0] * n
p = [0] * n
for i in range(n):
    t[i], p[i] = map(int, input().split())
ans = 0
def go(day, s):
    global ans
    if day == n:
        ans = max(ans, s)
        return
    if day > n:
        return
    go(day + t[day], s + p[day])
    go(day + 1, s)

go(0, 0)
print(ans)
