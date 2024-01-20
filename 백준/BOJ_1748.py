#문자열을 이용하여 수를 계속 붙여나가면서 새로운 수 만들기 -> 시간 복잡도 O(N)
#O(N) = 1억이므로 더 빠른 방법 필요 -> 수의 자리수별로 나누어서 문제 해결
#ex) N = 356이면 1 ~ 9는 길이가 1씩 증가, 10 ~ 99는 길이가 2씩 증가, 100 ~ 356은 길이가 3씩 증가
#ex) 따라서 정답은 (9 - 1 + 1) * 1 + (99 - 10 + 1) * 2 + (356 - 100 + 1) * 3
#위의 방법을 이용하면 N은 최대 1억(9자리수)이므로 최대 9번만 계산하면 정답을 구할 수 있음
#시간 복잡도는 O(N)이 아닌 O(lgN)
#length는 자리수, start는 자리수의 시작수, end는 자리수의 마지막수
#다음 자리수의 start는 현재 자리수의 start * 10, ex) length = 2 -> start = 1 * 10
#end는 다음 자리수의 start에서 -1, ex) length = 1 -> end = 1 * 10 - 1
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
n = int(input())
ans = 0
start = 1
length = 1
while start <= n:
    end = start * 10 - 1
    if end > n:
        end = n
    ans += (end - start + 1) * length
    start *= 10
    length += 1
print(ans)
