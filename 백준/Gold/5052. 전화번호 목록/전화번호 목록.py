
tc = int(input())

for _ in range(tc):

    n = int(input())
    nums = [input() for _ in range(n)]
    nums.sort()
    flag = True

    for i in range(n - 1):
        size = len(nums[i])

        if nums[i] == nums[i + 1][:size]:
            flag = False

    if flag:
        print("YES")
    else:
        print("NO")