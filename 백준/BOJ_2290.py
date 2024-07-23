#출력문은 위에서부터 -, |, -, |, - 모양으로 구성
#하나의 숫자를 표시하기 위해 7개의 그룹으로 나눠서 표현(각각의 그룹이 채워지거나 채워지지 않음)
#c는 숫자를 표현하기 위해 7개의 그룹에서 어디가 채워져야 하는지 미리 구해놓은 배열
#c의 0행은 숫자 0을 나타냄 -> 0은 0, 1, 2, 4, 5, 6번 그룹이 채워져야 하므로 값이 1
#i는 위에서부터 -, |, -, |, - 모양으로 출력하기 위해서 0 ~ 4까지 5번 반복
#i가 0, 2, 4 중 하나이면 - 모양에 대한 처리
#i가 1, 3 중 하나이면 | 모양에 대한 처리
#i와 c의 값에 따라 '-', '|', ' '중 하나를 출력
#위에서부터 한 줄씩 주어진 모든 숫자에 대한 모양 출력
#따라서 숫자 중간에 줄바꿈없이 출력하기 위해 sys.stdout.write 사용
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
print = sys.stdout.write
c = (
    (1, 1, 1, 0, 1, 1, 1),
    (0, 0, 1, 0, 0, 1, 0),
    (1, 0, 1, 1, 1, 0, 1),
    (1, 0, 1, 1, 0, 1, 1),
    (0, 1, 1, 1, 0, 1, 0),
    (1, 1, 0, 1, 0, 1, 1),
    (1, 1, 0, 1, 1, 1, 1),
    (1, 0, 1, 0, 0, 1, 0),
    (1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 0, 1, 1)
)
s, n = input().split()
s = int(s)
m = len(n)
for i in range(5):
    if i in [0, 2, 4]:
        for j in range(m):
            now = int(n[j])
            if j != 0:
                print(' ')
            print(' ')
            if (i == 0 and c[now][0]) or (i == 2 and c[now][3]) or (i == 4 and c[now][6]):
                print('-' * s)
            else:
                print(' ' * s)
            print(' ')
        print('\n')
    else:
        for l in range(s):
            for j in range(m):
                now = int(n[j])
                if j != 0:
                    print(' ')
                if (i == 1 and c[now][1]) or (i == 3 and c[now][4]):
                    print('|')
                else:
                    print(' ')
                print(' ' * s)
                if (i == 1 and c[now][2]) or (i == 3 and c[now][5]):
                    print('|')
                else:
                    print(' ')
            print('\n')
