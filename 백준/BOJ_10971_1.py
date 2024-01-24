#다음 순열(BOJ_10972.py) 이용
#N개의 도시를 방문하는 모든 순서를 만들어보고 각각의 순서마다 비용을 계산하여 최소값 구하기
#시간 복잡도는 모든 순열을 구하는 시간 복잡도와 같으므로 O(N * N!)
#2 <= N <= 10이므로 N * N! = 10 * 10! = 36288000, 1억보다 작으므로 모든 경우 다 해보기
#첫 순열은 0 ~ N-1의 도시를 차례대로 방문하는 경우
#d는 순서, d[i]는 i번째 방문하는 도시의 번호
#d[0], d[1], ..., d[N-1]의 순서대로 방문하다가 d[N-1]에서 d[0](출발점)으로 돌아오기
#ok는 이동이 가능한 지 체크하는 변수(i에서 i+1로 이동이 가능하면 True, 불가능하면 False)
#마지막에서 출발지로 돌아올 때는 ok가 True고 d[N-1]에서 d[0]으로 이동이 가능해야 함
#하나의 경로가 완성되면 비용(s)을 이전에 구한 정답(ans)과 비교하여 작으면 ans값 바꿔주기
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(a) - 1
    while a[j] <= a[i-1]:
        j -= 1

    a[i-1], a[j] = a[j], a[i-1]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
d = list(range(n))
ans = 2147483647
while True:
    ok = True
    s = 0
    for i in range(0, n-1):
        if w[d[i]][d[i+1]] == 0:
            ok = False
            break
        else:
            s += w[d[i]][d[i+1]]
    if ok and w[d[-1]][d[0]] != 0:
        s += w[d[-1]][d[0]]
        ans = min(ans, s)
    if not next_permutation(d):
        break
print(ans)
