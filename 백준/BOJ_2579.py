#d[i] : i번째 계단에 올랐을 때 얻을 수 있는 최대 점수
#계단을 1칸 올라서 i번째에 도착한 경우 i-3번째에서 2칸 오르고 i-1번째에서 1칸 오르기
#따라서 d[i] = d[i-3] + a[i-1] + a[i]
#계단을 2칸 올라서 i번째에 도착한 경우 i-2번째에서 2칸 오르기
#따라서 d[i] = d[i-2] + a[i]
#최대 점수를 구해야 하므로 d[i] = max(d[i-2], d[i-3] + a[i-1]) + a[i]
#d[1]은 1번째 계단에 올랐을 때 얻을 수 있는 최대 점수로 a[1]과 같음
#d[2]는 2번째 계단에 올랐을 때 얻을 수 있는 최대 점수로 1번째 계단에 오른 뒤 2번째 계단 오르기
#n=1일 때 a와 d를 [0] * (n+1)로 초기화하면 d[2] = d[1] + a[2]에서 index out of range 에러 발생
#따라서 n의 최대값이 300이므로 a와 d를 [0] * 301로 초기화
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
a = [0] * 301
d = [0] * 301
for i in range(1, n+1):
    a[i] = int(input())
d[1] = a[1]
d[2] = d[1] + a[2]
for i in range(3, n+1):
    d[i] = max(d[i-2], d[i-3] + a[i-1]) + a[i]
print(d[n])
