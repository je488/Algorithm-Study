#재귀함수 : 자기 자신을 호출하는 함수, 반복문 효과
#재귀함수가 작동할 때 스택 사용
#재귀함수가 작동할 때 스택에는 매개변수, 지역변수, 복귀주소 등이 기록됨 -> 스택프레임
#스택프레임 : 스택 영역에 차례대로 저장되는 함수의 호출정보(매개변수, 지역변수, 복귀주소 등)
#x가 0이면 함수 종료
#이진수를 구할 때 2로 나눈 나머지를 거꾸로 출력해야 하므로 DFS호출 뒤에 print()작성
import sys
# sys.stdin = open("input.txt", "r")
def DFS(x):
    if x == 0:
        return
    else:
        DFS(x // 2)
        print(x % 2, end='')

if __name__ == "__main__":
    n = int(input())
    DFS(n)
