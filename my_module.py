# # 비트 연산으로 부분집합 구하기
# def get_subset(arr, n):
#     subset_list = []
#     for i in range(1 << n):
#         subset_tmp = []
#         for j in range(n):
#             if i & (1 << j):
#                 subset_tmp.append(arr[j])
#         subset_list.append(subset_tmp)
#     return subset_list

# arr = [1, 2, 3, 4]
# n = len(arr)
# # print(get_subset)

# # 이진 탐색
# def binary_search(arr, target):
#     N = len(arr)
#     start = 0
#     end = N - 1

#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] == target:
#             return mid
        
#         if target < arr[mid]:
#             end = mid - 1
#         else:
#             start = mid + 1
    
#     return False


# # 선택 정렬
# def selection_sort(arr):
#     N = len(arr)
#     for i in range(N - 1):
#         min_idx = i
#         for j in range(i + 1, N):
#             if arr[min_idx] > arr[j]:
#                 min_idx = j
    
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]



# # DFS 스택 구현: 강사님
# def dfs_stack(graph, start):
#     visited = [0] * len(graph)
#     visited[start] = 1
#     stack = [start]
#     print(start, end=" ")

#     while stack:
#         for w in graph[start]:
#             if not visited[w]:
#                 stack.append(w)
#                 visited[w] = 1
#                 start = w
#                 print(start, end=" ")
#                 break
#         else:
#             stack.pop()
#             if stack:
#                 start = stack[-1]

# def iterative_dfs(start):
#     discovered = []
#     stack = [start]
#     while stack:
#         v = stack.pop()

#         if v not in discovered:
#             discovered.append(v)
#             for w in graph[v]:
#                 stack.append(w)
    
#     return discovered

# graph = {
#     0: [1, 2],
#     1: [0, 3, 4],
#     2: [0, 5],
#     3: [1],
#     4: [1],
#     5: [2]
# }

# dfs_stack(graph, 0)
# print(iterative_dfs(0))


# # 부분 집합
# def construct_candidates(c):
#     c[0] = True
#     c[1] = False
#     return 2

# def process_solution(a, k):
#     for i in range(k):
#         if a[i]:
#             print(num[i], end = ' ')
#         print()

# def backtrack(a, k, n):
#     c = [0] * MAXCANDIDATES
#     if k == n:
#         process_solution(a, k)
#     else:
#         ncandidates = construct_candidates(c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a, k + 1, n)

# MAXCANDIDATES = 2
# num = [1, 2, 3, 4]
# a = [0] * len(num)
# backtrack(a, 0, 4)



# # 순열 permutation
# def construct_candidates(a, k, n, c):
#     in_perm = [False] * (NMAX + 1)

#     for i in range(k):
#         in_perm[a[i]] = True

#     ncandidates = 0
#     for i in range(1, NMAX + 1):
#         if in_perm[i] == False:
#             c[ncandidates] = i
#             ncandidates += 1
#     return ncandidates

# def backtrack(a, k, n):
#     c = [0] * MAXCANDIDATES

#     if k == n:
#         for i in range(k):
#             print(a[i], end = ' ')
#         print()
#     else:
#         ncandidates = construct_candidates(a, k, n, c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a, k + 1, n)

# MAXCANDIDATES = 3 # 조합의 크기
# NMAX = 3 # 사용할 숫자의 값 (1부터 3까지)
# a = [0] * NMAX # 순열을 저장할 배열
# # backtrack(a, 0, 3)


def quick_sort(arr):
    def sort(start, end):
        if start >= end:
            return arr

        pivot_index = partition(arr, start, end)
        sort(start, pivot_index - 1)
        sort(pivot_index + 1, end)

    def partition(arr, start, end):
        pivot = start
        left = start + 1
        right = end

        while left <= right:
            while left <= end and arr[left] <= arr[pivot]:
                left += 1
            while right > start and arr[right] >= arr[pivot]:
                right -= 1
            
            if left > right:
                arr[right], arr[pivot] = arr[pivot], arr[right] # 전체 while문 탈출
            else:
                arr[left], arr[right] = arr[right], arr[left]
        
        return right

    sort(0, len(arr) - 1)
    return arr


def quick_sort_slicing(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    tail = arr[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort_slicing(left) + [pivot] + quick_sort_slicing(right)


def quick_sort_median_slicing(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left, mid, right = [], [], []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            mid.append(num)
    
    return quick_sort_median_slicing(left) + mid + quick_sort_median_slicing(right)


def quick_sort_median(arr):
    def sort(left, right):
        if left >= right:
            return
        
        pivot_index = partition(left, right)
        sort(left, pivot_index - 1)
        sort(pivot_index, right)
    
    def partition(left, right):
        pivot = arr[(left + right) // 2]
        while left <= right:
            while arr[left] < pivot:
                left += 1
            while arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        return left

    sort(0, len(arr) - 1)
    return arr

            
def merge_sort(arr):
    def merge(left, right):
        tmp = []
        l = r = 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                tmp.append(left[l])
                l += 1
            else:
                tmp.append(right[r])
                r += 1
        
        tmp += left[l:]
        tmp += right[r:]
        return tmp

    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge_sort_opt(arr):
    def sort(low, high):
        if high - low <= 1:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)
    
    def merge(low, mid, high):
        tmp = []
        l, h = low, high

        while l < mid and h < high:
            if arr[l] > arr[h]:
                tmp.append(arr[l])
                l += 1
            else:
                tmp.append(arr[h])
                h += 1
        while l < mid:
            tmp.append(arr[l])
            l += 1
        while h < high:
            tmp.append(arr[h])
            h += 1
        
        for i in range(low, high):
            arr[i] = tmp[i - low]
    
    return sort(0, len(arr))




arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# print(quick_sort(arr, 0, len(arr) - 1))
# print(quick_sort_slicing(arr))
# print(quick_sort_median(arr))
# print(quick_sort(arr))
print(merge_sort(arr))