A, B = map(int, input().split())

two_lst = []
for _ in range(2):
    two_lst += list(map(int, input().split())) #[1, 2, 4, 2, 3, 4, 5, 6]

result = len(set(two_lst)) - (len(two_lst) - len(set(two_lst)))
print(result)