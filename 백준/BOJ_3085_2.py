#BOJ_3085_1.py보다 빨리 푸는 방법
#가장 긴 연속 부분의 행 또는 열을 찾을 때 시간복잡도를 O(N^2)에서 O(N)으로 줄일 수 있음
#임의의 두 칸을 변경했을 때, 정답에 변화가 있는 것은 최대 3개의 행과 열이므로 O(3N) -> O(N)
#따라서 총 시간복잡도는 O(N^2 * N) = O(N^3)
#check 함수에 board와 검사할 행의 시작번호, 끝번호, 검사할 열의 시작번호, 끝번호를 넘겨줌
#check 함수에서 검사할 행과 열만 탐색하여 가장 긴 연속 부분을 찾음
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def check(board, start_row, end_row, start_col, end_col):
    n = len(board)
    ans = 1
    for i in range(start_row, end_row + 1):
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
    for i in range(start_col, end_col + 1):
        cnt = 1
        for j in range(1, n):
            if board[j][i] == board[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
    return ans

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        if j+1 < n:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            tmp = check(board, i, i, j, j+1)
            if ans < tmp:
                ans = tmp
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        if i+1 < n:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            tmp = check(board, i, i+1, j, j)
            if ans < tmp:
                ans = tmp
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
print(ans)
