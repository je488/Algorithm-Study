#서로 다른 정육면체의 전개도 개수는 11개이므로 11개를 소스에 추가해서 하나씩 검사해보기
#각각의 전개도 모양에서 대칭, 회전 가능/ 2번 대칭하면 원래 상태, 4번 회전하면 원래 상태
#원래 모양에서 회전 4번, 대칭한 상태에서 회전 4번 -> 전개도 모양마다 총 8개의 방법 검사
#cubes는 11개의 정육면체 전개도 모양을 나타낸 리스트
#mirror는 전개도를 대칭시키는 함수, rotate는 전개도를 90도 회전시키는 함수
#check는 a의 (x, y)부터 b의 크기만큼을 b와 비교하여 일치하는지 체크하는 함수
#a에서 전개도 모양이 어디에 위치한지 알 수 없으므로 a의 모든 좌표에 대해 검사
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
cubes = [
    ["0010",
     "1111",
     "0010"],
    ["0100",
     "1111",
     "1000"],
    ["0010",
     "1111",
     "0100"],
    ["0001",
     "1111",
     "1000"],
    ["0001",
     "1111",
     "0100"],
    ["11100",
     "00111"],
    ["1100",
     "0111",
     "0010"],
    ["1100",
     "0111",
     "0001"],
    ["0010",
     "1110",
     "0011"],
    ["0001",
     "1111",
     "0001"],
    ["1100",
     "0110",
     "0011"]
]

def mirror(b):
    ans = []
    for i in range(len(b)):
        tmp = b[i][::-1]
        ans.append(tmp)
    return ans

def rotate(b):
    ans = [''] * len(b[0])
    for j in range(len(b[0])):
        for i in range(len(b)-1, -1, -1):
            ans[j] += b[i][j]
    return ans

def check(a, b, x, y):
    n = len(a)
    for i in range(len(b)):
        for j in range(len(b[0])):
            nx = x + i
            ny = y + j
            if 0 <= nx < n and 0 <= ny < n:
                if b[i][j] == '0':
                    if a[nx][ny] == 1:
                        return False
                elif b[i][j] == '1':
                    if a[nx][ny] == 0:
                        return False
            else:
                return False
    return True

T = 3
for _ in range(T):
    n = 6
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    ans = False
    for cube in cubes:
        for mir in range(2):
            for rot in range(4):
                for i in range(n):
                    for j in range(n):
                        ans |= check(a, cube, i, j)
                cube = rotate(cube)
            cube = mirror(cube)
    print("yes" if ans else "no")
