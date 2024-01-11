#시간복잡도 : O(N^4)
#인접한 두 칸 고르기 -> O(N^2)
#한 칸을 고르고(N^2) 그 칸과 인접한 2칸 중 하나 고르기 -> O(N^2 * 2) = O(N^2)
#인접한 칸을 고를 때 4칸(상하좌우)이 아닌 2칸(오른쪽, 아래)만 탐색해도 전체 칸 모두 탐색 가능
#가장 긴 연속 부분의 행 또는 열 찾기 -> 전체 테이블을 모두 검사해야 하므로 -> O(N^2)
#따라서 총 시간복잡도는 O(N^2 * N^2) = O(N^4)
#check 함수는 입력으로 주어진 테이블 board에서 가장 긴 연속 부분의 행 또는 열을 찾음
#행과 열을 각각 따로 찾으며 이전 값과 비교하여 같으면 cnt += 1, 다르면 cnt = 1
#한 칸을 탐색할 때마다 이전에 구한 ans값과 cnt를 비교하여 cnt가 ans보다 크면 ans = cnt
#하나의 행 또는 열을 탐색한 뒤에 ans값과 cnt를 비교할 경우 가장 긴 연속 부분을 찾을 수 없음
#ex) 0행이 CCB인 경우 현재 ans는 2가 되어야 행을 모두 탐색한 뒤 비교하면 ans = 1
#인접한 두 칸을 교환하고 가장 긴 연속 부분의 행 또는 열을 찾은 뒤 다시 원래대로 교환해야 함★
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def check(board):
    n = len(board)
    ans = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
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
            tmp = check(board)
            if ans < tmp:
                ans = tmp
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        if i+1 < n:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            tmp = check(board)
            if ans < tmp:
                ans = tmp
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
print(ans)
