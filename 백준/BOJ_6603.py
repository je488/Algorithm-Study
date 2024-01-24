#다음 순열(BOJ_10972.py) 이용
#n개 중에서 6개를 고르면 n-6개는 고르지 않음
#고르지 않는 수를 0, 고르는 수를 1로 하여 d에 넣고 다음 순열(next_permutation) 구하기
#첫 순열은 0을 n-6개 넣고 1을 6개 넣은 순열 ex) n = 7이면 첫 순열은 0111111
#순열을 만들면 d[i]가 1인 경우에만(고른 경우에만) a[i]의 값을 cur(선택한 번호 조합)에 저장
#사전 순으로 출력하기 위해 cur을 ans에 저장하여 ans를 오름차순으로 정렬한 뒤 출력
#재귀 함수로도 풀 수 있음
#ex) n = 7, a = [1, 2, 3, 4, 5, 6, 7]
#ex) 첫 순열은 0111111 -> 1인 경우에만 그 위치의 a값을 cur에 저장 -> cur = [2, 3, 4, 5, 6, 7]
#ex) 다음 순열은 1011111 -> cur = [1, 3, 4, 5, 6, 7]
#ex) 그 다음 순열은 1101111 -> cur = [1, 2, 4, 5, 6, 7] -> 마지막 순열까지 반복
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

while True:
    n, *a = list(map(int, input().split()))
    if n == 0:
        break
    d = [0] * (n - 6) + [1] * 6
    ans = []
    while True:
        cur = [a[i] for i in range(n) if d[i] == 1]
        ans.append(cur)
        if not next_permutation(d):
            break
    ans.sort()
    for v in ans:
        print(' '.join(map(str, v)))
    print()
