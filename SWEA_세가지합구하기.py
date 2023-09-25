#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWEbPukqySUDFAWs(문제링크)
#for문 또는 range() 함수를 이용하여 합을 구하면 시간 초과가 발생하므로 등차수열의 합 공식 이용
#항의 개수가 n, 등차수열의 첫째항이 a, 끝항이 l인 경우 합 s는 n * (a+l) // 2
#l은 a + (n-1) * d와 같으므로 s = n * (2 * a + (n-1) * d) // 2
#s1은 n에 n, a에 1, d에 1을 대입하여 n * (n+1) // 2
#s2는 n에 n, a에 1, d에 2를 대입하여 n * n
#s3는 n에 n, a에 2, d에 2를 대입하여 n * (n+1)
#실행 시간을 단축시키기 위해 정답을 res 배열에 저장한 후 한꺼번에 출력
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
res = list()
for tc in range(1, T+1):
    n = int(input())
    s1 = n * (n+1) // 2
    s2 = n * n
    s3 = n * (n+1)
    res.append(f'#{tc} {s1} {s2} {s3}')
for r in res:
    print(r)
