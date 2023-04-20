N, M = map(int, input().split(" "))

# construct adjacency list (while reading input and counting in-degrees)
adjacency_list = [[] for _ in range(N+1)]
in_degree = [0 for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split(" "))
    adjacency_list[y].append(x)
    in_degree[x] += 1

# find all nodes with in-degree 0 - add to current layer.
# curret_layer is a list of nodes that only depend on nodes
# in previous layers (semesters) i.e. they can be taken in the current semester.
current_layer = []
for course in range(1, N+1):
    if in_degree[course] == 0:
        current_layer.append(course)

n_semesters = 0

# process the nodes in layers (semesters)
# each iteration of the outer loop corresponds to one semester
# - not one course.
while current_layer: # while there are nodes in the current layer,
                     # i.e. unprocessed nodes exist
    next_layer = [] # nodes that will have in-degree 0 in the next layer
    n_semesters += 1
    for course in current_layer:
        for dependent_course in adjacency_list[course]:
            in_degree[dependent_course] -= 1
            if in_degree[dependent_course] == 0:
                next_layer.append(dependent_course)
    current_layer = next_layer

print(n_semesters)