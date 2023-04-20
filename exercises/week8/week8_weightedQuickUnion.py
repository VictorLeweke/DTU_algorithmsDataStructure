N = int(input())
M = int(input())

u = [i for i in range(N)]
sz = [1]*N

def find(i,u):
    while i != u[i]:
        i = u[i]
    return i

def union(i,j,u):
    ri = find(i,u)
    rj = find(j,u)
    
    if ri != rj:
        if sz[ri] >= sz[rj]:
            u[rj] = ri
            sz[ri] += sz[rj]
        else:
            u[ri] = rj
            sz[rj] += sz[ri]
        
for _ in range(M):
    opr = input()
    
    if opr[0] == "F":
        print(find(int(opr.split()[1]),u))
    if opr[0] == "U":
        i, j = map(int,opr.split()[1:])
        union(i,j,u)


