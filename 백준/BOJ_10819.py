#다음 순열(BOJ_10972.py) 이용
#수의 순서를 변경할 수 있는 방법의 개수 : N!
#3 <= N <= 8이므로 N! = 8! = 40320, 방법의 수가 작으므로 모든 경우 다 해보기
#첫 순열을 만들고 마지막 순열이 나올 때까지 다음 순열을 구하는 함수(next_permutation) 호출
#첫 순열을 만들기 위해 주어진 N개의 수를 오름차순으로 정렬
#순열을 만들면 calc 함수로 문제에서 주어진 식의 값을 구하기
#식의 값이 이전에 구한 정답(ans)보다 크면 ans값 바꿔주기
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(a) - 1
    while a[j] <= a[i-1]:
        j -= 1

    a[i-1], a[j] = a[j], a[i-1]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

def calc(a):
    ans = 0
    for i in range(1, len(a)):
        ans += abs(a[i] - a[i-1])
    return ans

n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
while True:
    tmp = calc(a)
    ans = max(ans, tmp)
    if not next_permutation(a):
        break
print(ans)
