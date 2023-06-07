
def dfs(start, depth):
    if depth == 6:
        print(*result)
        return

    for i in range(start, len(nums)):
        result[depth] = nums[i]
        dfs(i+1, depth+1)

while True:
    nums = list(map(int, input().split()))

    if nums[0] == 0:
        break

    result = [0] * 6

    nums = nums[1:]
    
    dfs(0, 0)
    print()