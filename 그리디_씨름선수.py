#키를 기준으로 내림차순 정렬
#나보다 키가 큰 사람 중 몸무게가 큰 사람이 있을 경우 씨름 선수 탈락 -> 나보다 키가 큰 사람들보다 내 몸무게가 큰 경우, 씨름 선수 합격
#키는 정렬한 상태이므로 몸무게만 가지고 비교해서 내가 몸무게가 가장 크면 씨름 선수 합격 -> 몸무게를 가지고 최대값 찾는 것처럼(최대값이 바뀔때마다 카운트)
import sys
sys.stdin = open("input.txt", "r")
n = int(input())
info = []
for _ in range(n):
    height, weight = map(int, input().split())
    info.append((height, weight))
info.sort(reverse = True)
cnt = 0
max_value = 0
for height, weight in info:
    if weight > max_value:
        cnt += 1
        max_value = weight
print(cnt)
