
N = int(input())

nums = list(map(int, input().split()))
nums.sort()

answer = 0

for i in range(N):
    tmp = nums[:i] + nums[i+1:]
    s = 0
    e = len(tmp) - 1

    while s < e:
        total = tmp[s] + tmp[e]
        if total == nums[i]:
            answer += 1
            break
        elif total < nums[i]:
            s += 1
        else:
            e -= 1

print(answer)