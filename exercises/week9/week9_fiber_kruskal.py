def find(i, U):
    if i != U[i]:
        U[i] = find(U[i], U)
    return U[i]

def union(i, j, U, sz):
    rep_i = find(i, U)
    rep_j = find(j, U)
    if sz[rep_i] > sz[rep_j]:
        U[rep_j] = rep_i
        sz[rep_i] += sz[rep_j]
    else:
        U[rep_i] = rep_j
        sz[rep_j] += sz[rep_i]

N, M = map(int, input().split())

edges = [list(map(int, input().split())) for i in range(M)]
edges.sort(key = lambda x: x[2])

U = list(range(N+1))
sz = [1]*(N+1)

MST_weight = 0

for i, j, w in edges:
    if find(i,U) != find(j,U):
        union(i,j,U,sz)
        MST_weight += w

print(MST_weight)