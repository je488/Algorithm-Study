#재귀 함수 이용
#n개의 수를 각각 조합(로또 번호)에 넣을지 말지 결정 -> O(2^k)
#6 < k < 13이므로 k는 최대 12 -> 2^12 = 4096이므로 모든 경우 다 해보기
#index는 선택할지 말지 결정해야 하는 수의 인덱스, lotto는 선택한 숫자
#len(lotto) == 6이면 정답을 찾은 경우로 숫자 출력
#index == len(a)이면 더 이상 선택할지 말지 결정할 숫자가 없으므로 불가능한 경우 -> return
#정답을 찾은 경우가 불가능한 경우보다 앞에 위치해야 함
#ex) a의 마지막 수인 a[n-1]을 선택하고 n으로 넘어갈 때 cnt가 6이 되는 경우
#ex) index가 n이 되어 선택할지 말지 결정할 숫자가 없지만 cnt가 6이므로 정답을 찾은 경우에 해당
#사전 순으로 출력해야 하고 a는 오름차순으로 정렬된 상태
#따라서 index번째 수를 선택하는 경우부터 코드 작성
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def solve(a, index, lotto):
    if len(lotto) == 6:
        print(' '.join(map(str, lotto)))
        return
    if index == len(a):
        return
    solve(a, index+1, lotto+[a[index]])
    solve(a, index+1, lotto)

while True:
    n, *a = list(map(int, input().split()))
    if n == 0:
        break
    solve(a, 0, [])
    print()
