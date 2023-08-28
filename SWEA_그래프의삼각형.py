#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWbHcWd6AFcDFAV0(문제링크)
#line에 간선으로 이어진 두 개의 정점(x, y)을 키(정점)와 값(정점과 연결된 점들)으로 저장
#x, y는 y, x와 같은 간선을 의미하므로 키 y의 값에도 x 저장
#defaultdict로 기본값을 set으로 지정 -> 딕셔너리 value의 자료형이 set이 되므로 add로 값 추가
#defaultdict는 기존에 키가 없는 경우 기본값(set) 할당 -> 초기화할 필요없이 add 가능
#1부터 n까지 3개의 정점을 선택하여 모두 간선으로 이루어져 있는지 확인
#line[i], line[j], line[k]에는 각각의 정점(i, j, k)과 연결된 점들이 저장되어 있음
#따라서 i가 line[j]에 포함되어 있고 j가 line[k]에 포함되어 있고 k가 line[i]에 포함되어 있으면 삼각형
import sys
from collections import defaultdict
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    line = defaultdict(set)
    res = 0
    for _ in range(m):
        x, y = map(int, input().split())
        line[x].add(y)
        line[y].add(x)
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                if i in line[j] and j in line[k] and k in line[i]:
                    res += 1
    print(f'#{tc} {res}')
