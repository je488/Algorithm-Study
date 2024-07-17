#부연설명 참고
#1. 배열을 그룹지어 그룹별로 1차원 배열에 넣기
#2. 1차원 배열을 r번 회전
#3. 그룹별로 회전시킨 값을 다시 배열에 넣기
#0번 그룹은 가장 바깥쪽 그룹, k번 그룹은 가장 바깥쪽으로부터 k칸 떨어져 있음
#그룹을 위, 오른쪽, 아래, 왼쪽으로 나누어 순서대로 1차원 배열에 넣기
#k번 그룹의 위 : a[k][j] (k <= j < m-k) / 코드에서는 마지막 값의 중복 방지를 위해 k <= j < m-k-1
#k번 그룹의 오른쪽 : a[i][m-k-1] (k <= i < n-k) / 코드에서는 중복 방지를 위해 k <= i < n-k-1
#k번 그룹의 아래 : a[n-k-1][j] (k <= j < m-k) / 코드에서는 중복 방지를 위해 k < j < m-k
#k번 그룹의 왼쪽 : a[i][k] (k <= i < n-k) / 코드에서는 중복 방지를 위해 k < i < n-k
#1차원 리스트 a를 k번 회전해서 1차원 리스트 b를 만들었을 때 b[i] = a[k+i] % a의 크기
#ex) a = [1, 5, 2, 4, 3, 7]를 3번 회전하면 b = [4, 3, 7, 1, 5, 2] (3번 인덱스 값이 첫번째로)
#ex) 위의 예제에서 a를 3번 회전하고 i=3이면 b[3] = a[6]으로 index out of range
#ex) 따라서 a[k+i]를 a의 크기로 나눈 나머지 값을 b[i]에 넣기
#groupn은 그룹의 개수
#groups는 a의 모든 그룹을 포함한 리스트
#그룹별로 r번 회전시킨 값을 위, 오른쪽, 아래, 왼쪽 순서로 다시 a에 넣기
#배열의 크기가 5인데 5번 회전하는 경우 원래 배열과 같고 6번 회전하면 1번 회전하는 것과 같음
#따라서 index = r % l
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
groups = []
groupn = min(n, m) // 2
for k in range(groupn):
    group = []
    for j in range(k, m-k-1):
        group.append(a[k][j])
    for i in range(k, n-k-1):
        group.append(a[i][m-k-1])
    for j in range(m-k-1, k, -1):
        group.append(a[n-k-1][j])
    for i in range(n-k-1, k, -1):
        group.append(a[i][k])
    groups.append(group)

for k in range(groupn):
    group = groups[k]
    l = len(group)
    index = r % l
    for j in range(k, m-k-1):
        a[k][j] = group[index]
        index = (index+1) % l
    for i in range(k, n-k-1):
        a[i][m-k-1] = group[index]
        index = (index+1) % l
    for j in range(m-k-1, k, -1):
        a[n-k-1][j] = group[index]
        index = (index+1) % l
    for i in range(n-k-1, k, -1):
        a[i][k] = group[index]
        index = (index+1) % l

for row in a:
    print(' '.join(map(str, row)))
