def find(i,U):
    if U[i] != i:
        U[i] = find(U[i],U)
    return U[i]

def union(i,j,U,sz):
    i_id = find(i,U)
    j_id = find(j,U)
    if sz[i_id] > sz[j_id]:
        U[j_id] = i_id
        sz[i_id] += sz[j_id]
    else:
        U[i_id] = j_id
        sz[j_id] += sz[i_id]

N, M = map(int, input().split(" "))
U = [i for i in range(N)]
sz = [1 for i in range(N)]

for i in range(M):
    cmd, i, j = input().split(" ")
    i = int(i)
    j = int(j)
    if cmd == "C":
        if find(i,U) == find(j,U):
            print("YES")
        else:
            print("NO")
    else:
        union(i,j,U,sz)