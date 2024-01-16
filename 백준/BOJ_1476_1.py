#가능한 연도의 개수는 15 * 28 * 19 = 7980으로 모든 경우 다 해보기
#e, s, m을 1씩 더해주다가 각각 16, 29, 20이 되면 1로 값을 바꿔주기
#year도 1씩 더해주다가 e == E이고 s == S이고 m == M이면 그 때의 year 출력
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
E, S, M = map(int, input().split())
e, s, m = 1, 1, 1
year = 1
while True:
    if e == E and s == S and m == M:
        print(year)
        break
    e += 1
    s += 1
    m += 1
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1
    year += 1
