import sys
sys.stdin = open("정렬된배열에서특정수의개수구하기.txt", "r")


# n, x = map(int, input().split())
# array = list(map(int, input().split()))

# from bisect import bisect_left, bisect_right

# def get_count_by_bisect(array, x):
#     left = bisect_left(array, x)
#     right = bisect_right(array, x)
#     return right - left

# count = get_count_by_bisect(array, x)

# if count == 0:
#     print(-1)
# else:
#     print(count)

def count_by_value(array, x): # 정렬된 수열에서 값이 x인 원소의 개수를 세는 메서드
    n = len(array) # 데이터의 개수

    first_idx = first(array, x, 0, n-1) # x가 처음 등장한 인덱스

    if first_idx == None: # 수열에 x가 존재하지 않는 경우
        return 0 # 값이 X인 원소의 개수는 0개이므로 0 반환
    
    last_idx = last(array, x, 0, n-1) # x가 마지막으로 등장한 인덱스

    return last_idx - first_idx + 1

def first(array, target, start, end):

    if start > end:
        return None
    
    mid = (start + end) // 2

    # target == mid인 동시에, mid - 1은 target보다 작은 경우
    # 조건을 만족하는 가장 왼쪽에 있는 인덱스인 경우
    if target == array[mid] and (mid == 0 or target > array[mid - 1]):
        return mid
    
    elif target <= array[mid]:
        return first(array, target, start, mid - 1)
    
    else:
        return first(array, target, mid + 1, end)

def last(array, target, start, end):

    if start > end:
        return None
    
    mid = (start + end) // 2

    if array[mid] == target and (mid == 0 or array[mid + 1] > target):
        return mid
    
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    
    else:
        return last(array, target, mid + 1, end)

count = count_by_value(array, x)
print(count if count > 0 else -1)