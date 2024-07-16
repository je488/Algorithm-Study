#n개의 숫자가 부분수열에 포함되거나 포함되지 않으므로 전체 부분수열의 개수는 2^n
#크기가 양수인 부분수열은 모든 숫자가 부분 수열에 포함되지 않는 경우 1가지 제외 -> 2^n - 1
#n <= 20이므로 모든 경우의 수는 2^20 - 1 = 1048575, 1억보다 작으므로 모든 경우 다 해보기
#i는 부분수열에 포함할지 말지 결정해야 하는 숫자의 인덱스
#sum은 현재까지 부분수열의 합
#sum == s라고 해서 무조건 정답X
#ex) n = 10, s = 15, a[6] = 15, a[7] = 3, a[8] = -3, a[9] = 0
#ex) a[6]을 선택한 경우 sum = 15
#ex) a[6], a[7], a[8], a[9]를 선택한 경우에도 sum = 15
#따라서 n개에 대한 선택이 모두 끝난 뒤에(즉, index == n인 경우) 정답인지 불가능인지 체크
#크기가 양수가 아닌 부분수열(공집합)은 1가지로 합이 0
#따라서 s == 0인 경우 크기가 양수가 아닌 부분수열이 정답에 포함되어 있으므로 -1해서 출력
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, s = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
def go(i, sum):
    global ans
    if i == n:
        if sum == s:
            ans += 1
        return
    go(i+1, sum+a[i])
    go(i+1, sum)

go(0, 0)
if s == 0:
    ans -= 1
print(ans)
