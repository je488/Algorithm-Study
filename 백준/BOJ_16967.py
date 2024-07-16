#1 <= X, 1 <= Y 이므로 A[1][1]은 B[1][1]과 같다
#B[X+1][Y+1] = A[X+1][Y+1] + A[1][1]
#A[X+1][Y+1] = B[X+1][Y+1] - A[1][1]
#위의 식을 이용하여 원래 배열의 값 구하기
#코드에서는 원래 배열을 따로 만들지 않고 값만 변경한 후 H * W의 크기만큼만 출력
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
h, w, x, y = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h+x)]
for i in range(h):
    for j in range(w):
        a[i+x][j+y] -= a[i][j]
print(a)
for i in range(h):
    print(*a[i][:w])
