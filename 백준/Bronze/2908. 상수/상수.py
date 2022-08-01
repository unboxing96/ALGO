result = []
A, B = map(list, input().split())

A.reverse()
A_result = "".join(A)
result.append(A_result)

B.reverse()
B_result = "".join(B)
result.append(B_result)

print(max(result))