#각각의 사람마다 1번 팀 또는 2번 팀을 선택 -> 2^N
#N <= 20이므로 2^20 = 104876, 값이 1억보다 작으므 모든 경우 다 해보기
#first에는 1번 팀에 속한 사람의 번호, second에는 2번 팀에 속한 사람의 번호 저장
#t1은 first에 속한 팀원들의 능력치, t2는 second에 속한 팀원들의 능력치
#index == n인 경우 팀 배정이 끝났으므로 각 팀의 인원수가 n // 2인지 체크하고 능력치 구하기
#각 팀의 인원이 n // 2이 아닌 경우 -1을 리턴하고 인원수를 만족하면 두 팀의 능력치 차이 리턴
#능력치의 차이값을 리턴받으면 이전에 구한 정답(ans)과 비교하여 값이 작으면 ans값 바꿔주기
#함수 호출 전에 first나 second에 index를 추가하면 함수 호출 후에 index를 빼는 과정 필요
#파이썬의 경우 +를 이용하여 두 리스트를 합칠 수 있으므로 새로운 리스트를 만들어서 함수 호출
#따라서 first + []에서 first 자체는 변하지 않으므로 함수 호출 후에 index를 빼는 과정 필요X
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
