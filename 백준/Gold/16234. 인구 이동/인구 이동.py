class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root != y_root:
            if self.size[x_root] < self.size[y_root]:
                x_root, y_root = y_root, x_root
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]
            self.size[y_root] = 0


n, l, r = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(n)]

def get_union_population(unions):
    total_population = 0
    for union in unions:
        population = 0
        for i, j in union:
            population += countries[i][j]
        total_population += population // len(union)
        for i, j in union:
            countries[i][j] = population // len(union)
    return total_population


def get_unions():
    unions = []
    uf = UnionFind(n*n)

    for i in range(n):
        for j in range(n):
            if j < n-1:
                diff = abs(countries[i][j] - countries[i][j+1])
                if l <= diff <= r:
                    uf.union(i*n+j, i*n+(j+1))

            if i < n-1:
                diff = abs(countries[i][j] - countries[i+1][j])
                if l <= diff <= r:
                    uf.union(i*n+j, (i+1)*n+j)

    roots = {}
    for i in range(n):
        for j in range(n):
            root = uf.find(i*n+j)
            if root not in roots:
                roots[root] = []
            roots[root].append((i, j))

    for root in roots.values():
        if len(root) > 1:
            unions.append(root)

    return unions


days = 0
while True:
    unions = get_unions()
    if not unions:
        break
    get_union_population(unions)
    days += 1

print(days)
