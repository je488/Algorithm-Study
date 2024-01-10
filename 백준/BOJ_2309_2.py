#BOJ_2309_1.py보다 빠르게 푸는 방법
#난쟁이의 키는 변하지 않으므로 9명의 키의 합을 total에 저장
#i, j로 2명을 고르면 total - a[i] - a[j]는 나머지 7명의 키의 합 -> 시간복잡도 O(1)
#따라서 총 시간복잡도는 O(N^2 * 1) = O(N^2)
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = 9
a = [int(input()) for _ in range(n)]
a.sort()
total = sum(a)
for i in range(n):
    for j in range(i+1, n):
        if total - a[i] - a[j] == 100:
            for k in range(n):
                if i == k or j == k:
                    continue
                print(a[k])
            sys.exit(0)
