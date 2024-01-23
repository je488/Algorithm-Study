#첫 순열을 만들어서 출력하고 다음 순열을 구하는 함수(next_permutation) 호출
#next_permutation 함수가 False를 리턴할 때까지(다음 순열이 없을 때까지) 반복
#첫 순열은 1 ~ N을 오름차순(비내림차순)으로 정렬해서 구하기
#시간 복잡도는 다음 순열(O(N))의 연산을 순열의 개수(N!)만큼 해야하므로 O(N * N!)
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

n = int(input())
a = list(range(1, n+1))
while True:
    print(' '.join(map(str, a)))
    if not next_permutation(a):
        break
