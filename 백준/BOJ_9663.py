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