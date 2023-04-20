N = int(input())
M = int(input())

u = [i for i in range(N)]

def find(i,u):
    return u[i]

def union(i,j,u):
    if u[i] != u[j]:
        ri = find(i,u)
        rj = find(j,u)

        for k in range(N):
            if u[k] == ri:
                u[k] = rj

for _ in range(M):
    opr = input()
    if opr[0] == "F":
        print(find(int(opr.split()[1]),u))
    if opr[0] == "U":
        i, j = map(int,opr.split()[1:])
        union(i,j,u)




