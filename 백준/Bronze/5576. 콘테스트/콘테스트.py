team = []

for _ in range(20):
    team.append(int(input()))
A = team[:10]
B = team[10:]
A.sort()
B.sort()
A_result = A[-3] + A[-2] + A[-1]
B_result = B[-3] + B[-2] + B[-1]
print(A_result, B_result)