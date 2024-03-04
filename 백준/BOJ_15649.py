#go는 0번째부터 m-1번째까지 m개의 자리가 있을 때 각각의 자리에 올 수 있는 수를 정해주는 함수
#a는 수열을 저장하는 리스트, check는 숫자의 사용 여부를 체크하는 리스트
#idx == m이면 수열의 마지막 자리인 m-1번째 수를 정하고 다음을 호출한 경우이므로 수열 출력 후 종료
#check[i]값이 1이면 i는 이미 사용한 수이므로 건너뛰기
#check[i]값이 0이면 a의 idx번째에 i를 저장하고 check[i]값을 1로 바꿔서 i를 사용했음을 표시
#idx+1번째의 수를 결정하기 위해 go(idx+1) 호출
#go(idx+1) 호출이 끝나면 idx번째에 i가 온 다음에 일어날 모든 일은 go(idx+1)에서 모두 처리
#따라서 idx번째에는 현재의 i가 아닌 다른 수가 와야하므로 check[i] = 0으로 사용하지 않았음을 표시
#시간 복잡도는 1 <= M <= N <= 8이므로 M == N이라면 N * (N-1) * (N-2) * ... * 1 -> O(N!)
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n, m = map(int, input().split())
a = [0] * m
check = [0] * (n+1)
def go(idx):
    if idx == m:
        sys.stdout.write(' '.join(map(str, a)) + '\n')
        return
    for i in range(1, n+1):
        if check[i] == 1:
            continue
        check[i] = 1
        a[idx] = i
        go(idx+1)
        check[i] = 0

go(0)
