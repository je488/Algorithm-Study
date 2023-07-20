#지금까지 몬스터를 n번 때렸을 때 다음 공격의 데미지는 D(1+n*L%)이므로 sum에 데미지의 누적 합 구하기
#첫번째 공격을 할 때의 데미지는 D(1+0*L%)이고 N번째 공격을 할 때의 데미지는 D(1+(N-1)*L%)
#%는 1/100이므로 0.01 곱하기
#반복문 대신 수학식으로 한 번에 푸는 방법도 존재(부연설명 참고)
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    D, L, N = map(int, input().split())
    i = 0
    sum = 0
    for i in range(N):
        sum += D*(1+(i*L*0.01))
    print(f'#{tc} {int(sum)}')
