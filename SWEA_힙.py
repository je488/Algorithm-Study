#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV-Tj7ya3jYDFAXr(문제링크)
#리스트를 이용하여 최대 힙 구현
#특정 노드 번호가 x일 때 x의 부모 노드 번호 = x // 2
#특정 노드 번호가 x일 때 x의 왼쪽 자식 노드 번호 = x * 2, 오른쪽 자식 노드 번호 = x * 2 + 1
#위의 2가지 성질을 만족하기 위해서는 루트 노드의 번호가 1이어야 하므로 heap = [0]으로 초기화
#insert는 연산 1을 수행하는 함수로 val을 힙에 삽입
#delete는 연산 2를 수행하는 함수로 힙에서 최댓값 반환
#insert 함수에서 val을 삽입한 뒤에 부모 노드와 자식 노드 간에 대소관계가 성립하는지 체크
#idx는 현재 위치의 인덱스로 초기값은 heap의 마지막 인덱스, parent는 현재 위치의 부모 인덱스
#부모 노드값이 val보다 작으면 현재 위치에 부모 노드 값 넣고 현재 인덱스를 부모 인덱스로 바꾸기
#위 내용을 루트 노드까지 반복하고 반복문 종료 후 현재 위치에 val 값 넣기
#delete 함수에서 heap의 길이가 1이면 힙에 원소가 없는 경우로 -1 리턴
#heap에 원소가 있으면 루트 노드 값(리턴할 값)를 res에 저장하고 마지막 노드 값을 tmp에 저장
#삭제 후 루트 노드부터 마지막 노드까지 부모노드와 자식노드의 대소관계가 성립하는지 체크
#idx는 현재 위치의 인덱스로 초기값은 1(루트 노드)
#현재 위치의 왼쪽 자식과 오른쪽 자식 중 더 큰 값의 노드 번호를 cidx에 저장
#tmp가 heap[cidx](자식 중 더 큰 값)보다 작으면 현재 위치에 heap[cidx] 넣기
#또한 현재 인덱스를 cidx로 변경하고 반복문 종료 후 현재 위치에 tmp 값 넣기
import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
def insert(val):
    heap.append(val)
    idx = len(heap) - 1
    while idx > 1:
        parent = idx // 2
        if heap[parent] < val:
            heap[idx] = heap[parent]
            idx = parent
        else:
            break
    heap[idx] = val

def delete():
    if len(heap) == 1:
        return -1
    res = heap[1]
    tmp = heap[-1]
    idx = 1
    while idx * 2 < len(heap) - 1:
        if heap[idx * 2] > heap[idx * 2 + 1]:
            cidx = idx * 2
        else:
            cidx = idx * 2 + 1
        if tmp < heap[cidx]:
            heap[idx] = heap[cidx]
            idx = cidx
        else:
            break
    heap[idx] = tmp
    heap.pop()
    return res

T = int(input())
for tc in range(1, T+1):
    heap = [0]
    n = int(input())
    ans = list()
    ans.append('#' + str(tc))
    for _ in range(n):
        calc, *val = map(int, input().split())
        if calc == 1:
            insert(val[0])
        elif calc == 2:
            res = delete()
            ans.append(res)
    print(*ans)
