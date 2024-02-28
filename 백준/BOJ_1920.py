#for문을 사용하여 li2에 있는 수가 li1에 있는지 하나씩 확인하면 시간초과 -> 이분 탐색 이용
#이분 탐색을 이용하기 위해 li1을 오름차순으로 정렬
#binary_search(i)는 i가 li1에 존재하면 True, 존재하지 않으면 False 리턴
#mid는 li1의 중앙에 있는 값의 인덱스로 (start + end) // 2로 구하기
#i가 li1[mid]와 같으면 i가 li1에 존재하므로 True 리턴
#i가 li1[mid]보다 작으면 end값을 mid-1로 변경하여 start ~ mid-1 범위에서 값 찾기
#i가 li2[mid]보다 크면 start값을 mid+1로 변경하여 mid+1 ~ end 범위에서 값 찾기
#start > end가 되면 i가 li1에 존재하지 않으므로 반복을 종료하고 False 리턴
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def binary_search(i):
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        if li1[mid] == i:
            return True
        elif li1[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
    return False

n = int(input())
li1 = list(map(int, input().split()))
li1.sort()
m = int(input())
li2 = list(map(int, input().split()))
for i in li2:
    if binary_search(i):
        print(1)
    else:
        print(0)
