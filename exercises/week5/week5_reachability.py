#Take input
N,M,a,b = map(int,input().split())

#We add one to N, since our arrays are 0-indexed
#And the edges we are given in input are 1-indexed
N+=1

#Create adjacency list
adj = [[] for _ in range(N)]

#Read edges from input
for _ in range(M):
    x,y = map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)


#BFS a la CSES book 
from collections import deque
def bfs(adj,s,t):
    q = deque()

    visited = [False for _ in range(N)]

    visited[s] = True
    q.append(s)

    while(q):
        current = q.popleft()

        for neighbour in adj[current]:
            if(visited[neighbour]):
                continue
            if(neighbour == t):
                return True
            visited[neighbour] = True
            q.append(neighbour)

    return False

if(bfs(adj,a,b)):
    print("YES")
else:
    print("NO")

