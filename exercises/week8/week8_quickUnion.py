N = int(input())
M = int(input())

u = [i for i in range(N)]

def find(i,u):
    while i != u[i]:
        i = u[i]
    return i

def union(i,j,u):
    ri = find(i,u)
    rj = find(j,u)
    if ri != rj:
        u[ri] = rj

for _ in range(M):
    opr = input()
    if opr[0] == "F":
        print(find(int(opr.split()[1]),u))
    if opr[0] == "U":
        i, j = map(int,opr.split()[1:])
        union(i,j,u)