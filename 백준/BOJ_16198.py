#에너지 구슬은 첫번째와 마지막을 고를 수 없을 뿐 무엇을 골라야 할지 모르므로 다 해보기
#N개의 에너지 구슬이 있을 때 에너지 구슬을 고르는 방법의 수는 (N-2) * (N-3) * ... * 1 = (N-2)!
#N <= 10이므로 8! = 40320, 방법의 수가 크지 않으므로 모든 방법 다 해보기
#go(a)는 에너지 구슬의 무게가 a에 저장되어 있을 때 모을 수 있는 에너지의 최댓값을 리턴하는 함수
#n은 a의 크기로 2가 되면 더 이상 에너지를 모을 수 없으므로 0 리턴
#i는 제거할 구슬의 번호, energy는 i번 구슬을 제거하면 얻을 수 있는 에너지
#브루트 포스는 준비 -> 호출 -> 복원의 단계로 이루어짐
#준비를 하기 위해 새로운 변수를 만들어 함수를 호출하면 복원할 필요X
#따라서 a를 바꾸지 않고 구슬을 제거한 b를 따로 생성하여 함수 호출(a를 복원할 필요X)
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def go(a):
    n = len(a)
    if n == 2:
        return 0
    ans = 0
    for i in range(1, n-1):
        energy = a[i-1] * a[i+1]
        b = a[:i] + a[i+1:]
        energy += go(b)
        if ans < energy:
            ans = energy
    return ans

n = int(input())
a = list(map(int, input().split()))
print(go(a))
