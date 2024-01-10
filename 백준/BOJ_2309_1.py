#시간복잡도 : O(N^3)
#9명 중 2명을 찾아 나머지 7명의 키의 합을 계산
#9명 중 2명 찾기 -> 9C2 -> O(N^2)
#나머지 7명의 키의 합 계산하기 -> O(N)
#따라서 총 시간복잡도는 O(N^3)
#i, j로 2명을 고르고 k로 나머지 7명의 합(total)
#total이 100인 경우 i, j로 고른 2명을 제외한 나머지 7명의 키를 출력
#정답이 여러가지인 경우 아무거나 한가지만 출력하면 되므로 7명의 키를 출력한 뒤 프로그램 종료
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = 9
a = [int(input()) for _ in range(n)]
a.sort()
for i in range(n):
    for j in range(i+1, n):
        total = 0
        for k in range(n):
            if i == k or j == k:
                continue
            total += a[k]
        if total == 100:
            for k in range(n):
                if i == k or j == k:
                    continue
                print(a[k])
            sys.exit(0)
