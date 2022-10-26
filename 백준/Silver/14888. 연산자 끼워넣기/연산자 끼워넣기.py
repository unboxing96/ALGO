from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))

op = ["+", "-", "*", "/"]

oper_list = []
for i in range(4):
    for _ in range(opers[i]):
        oper_list.append(op[i])


answer = []

oper_set_list = list(set(permutations(oper_list)))
for oper_set in oper_set_list: # oper_set = ["+", "+", "-", "/", "*"]
    n = nums[0]
    for i in range(len(nums)-1): # i = 0, 1, 2, 3, 4
        if oper_set[i] == "+":
            n += nums[i+1]
        elif oper_set[i] == "-":
            n -= nums[i+1]
        elif oper_set[i] == "*":
            n *= nums[i+1]
        elif oper_set[i] == "/":
            if n // nums[i+1] < 0:
                n = -(-n // nums[i+1])
            else:
                n //= nums[i+1]
        
    answer.append(n)

print(max(answer))
print(min(answer))