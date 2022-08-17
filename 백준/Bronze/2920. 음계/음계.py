num_list = list(map(int, input().split()))

if num_list == list(range(num_list[0], num_list[-1] + 1)):
    print("ascending")
elif num_list == list(range(num_list[0], num_list[-1] - 1, - 1)):
    print("descending")
else:
    print("mixed")