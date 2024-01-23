#현재 순열이 무엇으로 시작하는 마지막 순열인지 알아보고 그 다음으로 시작하는 첫 순열 만들기
#ex) 1 3 4 2의 다음 순열 구하기 -> 1 3 4 2는 13으로 시작하는 마지막 순열
#ex) 13 다음은 14 -> 14로 시작하는 첫 순열은 1 4 2 3 -> 1 3 4 2의 다음 순열은 1 4 2 3
#다음 순열 찾는 방법
#1. A[i-1] < A[i]를 만족하는 가장 큰 i 찾기(순열의 뒤부터 내림차순이 얼마나 연속되는지 찾기)
#2. j >= i이면서 A[j] > A[i-1]를 만족하는 가장 큰 j 찾기
#즉, i-1번째 수보다 뒤에 있으면서 i-1번째 수보다 큰 수 중 가장 작은 수 찾기
#3. A[i-1]과 A[j]를 swap
#4. A[i]부터 끝까지 순열 뒤집기
#next_permutation은 순열 a의 다음 순열이 존재하면 True, 존재하지 않으면 False 리턴
#i를 찾는 데 걸리는 시간 : O(N)
#j를 찾는 데 걸리는 시간 : O(N)
#i-1번째 수와 j번째 수를 교환하는 데 걸리는 시간 : O(1)
#i ~ N까지 뒤집는 데 걸리는 시간 : O(N)
#총 시간 복잡도는 위에서부터 순서대로 진행하므로 모두 더하면 O(N)
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
a = list(map(int, input().split()))
if next_permutation(a):
    print(' '.join(map(str, a)))
else:
    print(-1)
