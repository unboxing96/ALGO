# def solution(n, lost, reserve):
#     for i in range(len(reserve)):
#         if reserve[i] in lost:
#             del lost[lost.index(reserve[i])]

#     for i in range(len(reserve)):
#         if reserve[i] - 1 in lost and reserve[i] - 1 in range(1, n + 1):
#             del lost[lost.index(reserve[i] - 1)]
#         elif reserve[i] + 1 in lost and reserve[i] + 1 in range(1, n + 1):
#             del lost[lost.index(reserve[i] + 1)]

#     else:
#         answer = n - len(lost)
#     return answer


# n = 5
# lost = [1, 4, 5]
# reserve = [3, 4]

# print(solution(n, lost, reserve))

print([1, 2, 3, 4] - [1, 2])
