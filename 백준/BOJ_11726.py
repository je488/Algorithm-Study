#D[n] : 2 * n 직사각형을 채우는 방법의 수
#2 * n 직사각형에서 가장 오른쪽에 타일을 놓을 수 있는 방법은 2가지
#1번째 방법은 2 * (n-1)에 타일을 채운 상태에서 가장 오른쪽에 1 * 2 타일 넣기
#2번째 방법은 2 * (n-2)에 타일을 채운 상태에서 가장 오른쪽에 2 * 1 타일 2개 넣기
#D[n] = D[n-1] + D[n-2]
#나머지 연산이 없는 경우 정답의 범위가 int, long을 넘어감
#따라서 d[i]의 값을 구할 때마다 나머지 연산으로 오버플로우 방지
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
d = [0] * 1001
d[0] = 1
d[1] = 1
for i in range(2, n + 1):
    d[i] = d[i - 1] + d[i - 2]
    d[i] %= 10007
print(d[n])
