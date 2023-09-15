#이것이 취업을 위한 코딩테스트다 - 115p
#모든 시각의 경우를 하나씩 모두 세서 '3'이 포함되어 있는지 확인하는 완전 탐색 문제
#하루는 86400(24 * 60 * 60)초로 경우의 수가 100만 개 이하이므로 완전 탐색 사용
#h를 입력받아 3중 반복문을 이용하여 00시 00분 00초부터 h시 59분 59초 사이의 시각을 모두 확인
#time은 시, 분, 초를 문자열로 변환하여 합친 값으로 '3'이 포함되어 있으면 res += 1
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
h = int(input())
res = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            time = str(i) + str(j) + str(k)
            if '3' in time:
                res += 1
print(res)
