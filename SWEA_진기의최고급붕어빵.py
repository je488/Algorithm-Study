#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LsaaqDzYDFAXc(문제링크)
#손님이 도착하는 시간은 정렬된 상태로 주어지지 않으므로 오름차순 정렬
#m초마다 k개의 붕어빵을 만들 수 있으므로 x초까지 만들 수 있는 붕어빵의 개수는 (x // m) * k
#bread는 a[i]초까지 만들 수 있는 붕어빵의 개수
#i+1은 a[i]초까지 붕어빵을 사가는 손님의 수
#손님이 도착하는 시간마다 만들 수 있는 붕어빵의 개수를 구하고 그 때까지 사가는 손님의 수와 비교
#bread < i+1이면 a[i]초까지 만들 수 있는 붕어빵의 개수가 손님의 수보다 작으므로 Impossible
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 'Possible'
    for i in range(n):
        bread = (a[i] // m) * k
        if bread < i+1:
            ans = 'Impossible'
            break
    print(f'#{tc} {ans}')
