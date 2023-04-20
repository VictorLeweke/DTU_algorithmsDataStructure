from heapq import heappush, heappop

N, M = map(int, input().split(" "))

# The graph is represented as an adjacency list
# The adjacency list is a list of lists of tuples
# Each tuple is of the form (node, weight)

adj_list = [[] for i in range(N+1)]
pointer = [None for i in range(N+1)] # called pi in the slides
key = [float("inf") for i in range(N+1)]

for i in range(M):
    u,v,w = map(int, input().split(" "))
    adj_list[u].append((v,w))
    adj_list[v].append((u,w))

# The priority queue is a list of tuples
# Each tuple is of the form (key, node)

MST = []

# insert first element
pq = [(0, 1)]
key[1] = 0

while pq:
    # extract min
    k, u = heappop(pq)

    # if the key, k, extracted from the heap is greater than the key of the node,
    # then the node has already been processed, and should be ignored.
    # otherwise, the node has not been processed, and should be
    # processed and added to the MST
    if key[u] == k:
        # iterate over neighbors to the priority queue
        for v, w in adj_list[u]:
            # if a smaller key is discovered, update the key and pointer
            # and add the node (neighbour) to the priority queue
            if w < key[v]:
                key[v] = w
                pointer[v] = u
                heappush(pq, (w, v))
        # add node to the MST and update the key to 0
        # so that it is not processed again
        MST.append((pointer[u], u, k))
        key[u] = 0

print(sum([w for u,v,w in MST]))



