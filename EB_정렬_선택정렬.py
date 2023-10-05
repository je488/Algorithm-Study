#이것이 취업을 위한 코딩테스트다 - 161p
#데이터가 N개일 때 가장 작은 값을 선택해서 맨 앞으로 보내는 과정을 N-1번 반복
#매번 가장 작은 값을 찾기 위해 비교 연산 필요
#시간 복잡도는 O(N²)으로 다른 정렬 알고리즘과 비교했을 때 비효율적
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[j] < array[min_index]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
print(array)
