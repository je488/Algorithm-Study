#divisor는 N의 진짜 약수가 모두 담긴 리스트
#따라서 divisor의 최소값과 최대값을 곱해주면 N
#시간복잡도는 N의 진짜 약수가 M개라고 할 때 O(M+M) = O(2M) = O(M)
#만약 N의 진짜 약수가 일부만 주어졌을 경우 최소값 * 최대값으로 풄 수 없음
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
cnt = int(input())
divisor = list(map(int, input().split()))
print(min(divisor) * max(divisor))
