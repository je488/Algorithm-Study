#현재 순열이 무엇으로 시작하는 첫 순열인지 알아보고 그 이전으로 시작하는 마지막 순열 만들기
#ex) 1 4 2 3의 이전 순열 구하기 -> 1 4 2 3는 14으로 시작하는 첫 순열
#ex) 14 이전은 13 -> 13로 시작하는 마지막 순열은 1 3 4 2-> 1 4 2 3의 다음 순열은 1 3 4 2
#이전 순열 구하는 방법 : 다음 순열을 구하는 과정에서 부등호를 반대로 바꾸기
#1. A[i-1] > A[i]를 만족하는 가장 큰 i 찾기(순열의 뒤부터 오름차순이 얼마나 연속되는지 찾기)
#2. j >= i이면서 A[j] < A[i-1]를 만족하는 가장 큰 j 찾기
#즉, i-1번째 수보다 뒤에 있으면서 i-1번째 수보다 작은 수 중 가장 큰 수 찾기
#3. A[i-1]과 A[j]를 swap
#4. A[i]부터 끝까지 순열 뒤집기
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def prev_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i-1] <= a[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(a) - 1
    while a[j] >= a[i-1]:
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
if prev_permutation(a):
    print(' '.join(map(str, a)))
else:
    print(-1)
