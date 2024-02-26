#퀸은 가로, 세로, 대각선으로 원하는 만큼 이동이 가능
#따라서 하나의 가로, 세로, 대각선에 퀸을 1개씩만 놓을 수 있음
#go(row)는 row행에서 퀸을 어디에 놓을지 결정하는 함수
#row가 n이 되면 n개의 퀸을 배치하는 한가지 방법이 완성되었으므로 return 1
#check는 row, col 자리에 퀸을 놓을 수 있는지 검사하는 함수
#check 함수에서 반복문을 이용하여 세로, 왼쪽대각선, 오른쪽대각선을 각각 검사하면 시간초과 발생
#따라서 check_col, check_dig, check_dig2 리스트를 이용하여 세로와 대각선에 놓을 수 있는지 검사
#check_col[i]는 i번 열에 퀸이 놓여져 있으면 1, 놓여져 있지 않으면 0
#check_dig[i]는 i번째 /대각선에 퀸이 놓여져 있으면 1, 놓여져 있지 않으면 0
#check_dig2[i]는 i번째 \대각선에 퀸이 놓여져 있으면 1, 놓여져 있지 않으면 0
#/대각선은 row+col값이 같으면 같은 대각선, \대각선은 n-1+row-col값이 같으면 같은 대각선
#check 함수를 이용하여 row, col 자리에 퀸을 놓을 수 있는지 검사 후 go 함수 호출
#go 함수의 호출이 끝나면 check_col, check_dig, check_dig2의 값을 다시 0으로 바꿔주기
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def check(row, col):
    if check_col[col]:
        return False
    if check_dig[row+col]:
        return False
    if check_dig2[n-1+row-col]:
        return False
    return True

def go(row):
    ans = 0
    if row == n:
        return 1
    for col in range(n):
        if check(row, col):
            check_col[col] = 1
            check_dig[row+col] = 1
            check_dig2[n-1+row-col] = 1
            ans += go(row+1)
            check_col[col] = 0
            check_dig[row+col] = 0
            check_dig2[n-1+row-col] = 0
    return ans

n = int(input())
check_col = [0] * n
check_dig = [0] * (2*n-1)
check_dig2 = [0] * (2*n-1)
print(go(0))
