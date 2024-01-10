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