#k : <x, y> 형태에서 각각 1씩 빼면 x는 k를 m으로 나눈 나머지, y는 k를 n으로 나눈 나머지
#전체 경우의 수는 1 <= M, N <= 40000이므로 MN = 16억 -> 문제 풀기에 적합하지 않음
#따라서 모든 경우를 만들어보지 않고 x를 이용하여 i * M + x(i >= 0)의 경우에만 검사
#시간 복잡도는 O(MN)이 아닌 O(N)
#ex) m = 5, n = 7, x = 4, y = 3인 경우 x와 y에서 각각 1씩 빼면 x = 3, y = 2
#ex) k % 5 = 3이므로 k가 될 수 있는 것은 3, 8, 13, 18, 23, ...
#ex) y = 2이므로 k % 7 = 2도 만족해야 함 -> k = 23
#ex) 처음에 1씩 빼서 구했으므로 k에 1을 더해서 정답은 24
#k의 초기값을 x로 두고 m씩 더해가면서 k % n = y가 되는 경우 찾기
#멸망년도는 m과 n의 최소공배수지만 반복문의 조건을 k < m * n으로 설정
#반복문은 시간복잡도가 O(N)이므로 최대 N번 수행, N은 40000이하의 작은 값
#따라서 반복문의 조건을 m과 n의 최소공배수를 구하지 않고 m * n으로 설정해도 무방
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    m, n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    k = x
    while k < m * n:
        if k % n == y:
            print(k + 1)
            break
        k += m
    else:
        print(-1)
