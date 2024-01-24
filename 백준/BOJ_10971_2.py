#BOJ_10971_1.py보다 빠른 방법
#경로가 1234, 2341, 3412, 4123이면 4가지는 모두 같은 경로(출발점으로 다시 돌아가야 하므로)
#따라서 시작점을 1로 고정시키면 전체 방법의 수는 N!이 아닌 N! / N이므로 (N-1)!
#총 시간 복잡도는 O(N * (N-1)!) = O(N!)
#next_permutation 함수로 다음 순열을 구했을 때 첫 번째 도시가 0이 아닌 1로 바뀌면 탐색 종료
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
    if d[0] != 0:
        break
print(ans)
