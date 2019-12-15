def dfs_stack(graph, start, goal, list):
    visited = set()
    expanded = []
    stack = [start]

    while stack:
        path = stack.pop()
        current_node = path[-1]
        expanded.append(path[-1])

        if current_node not in visited:
            visited.add(current_node)

        if current_node == goal:
            return path, expanded

        neighbours = graph[current_node]
        neighbour = reversed(neighbours)
        for j in neighbour:
            if j not in visited:
                appends = path + j
                stack.append(appends)



maps = {'a':0, 'b': 1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'p':8, 'q':9,  'r':10, 's':11 }
def dfs_stack_matrix(graph, start, goal, list):
    visited = set()
    expanded = []
    stack = [start]

    while stack:
        path = stack.pop()
        current_node = path[-1]
        expanded.append(path[-1])

        if current_node not in visited:
            visited.add(current_node)

        if current_node == goal:
            return path, expanded

        length = len(graph[maps[current_node]])
        for neighbor in range(length):
            reverse = length - 1 - neighbor
            if reverse not in visited and graph[maps[current_node]][reverse] == 1:
                    j = [k for k,v in maps.items() if v == reverse]
                    if j[0] not in visited:
                        appends = path + j[0]
                        stack.append(appends)




graph1 = {
    'a': ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a', 'd', 'f'],
    'd': ['b', 'c', 'e', 's'],
    'e': ['d', 'h', 'r', 's'],
    'f': ['c', 'g', 'r'],
    'g': ['f'],
    'h': ['e', 'p', 'q'],
    'p': ['h', 'q', 's'],
    'q': ['h', 'p'],
    'r': ['e', 'f'],
    's': ['d', 'e', 'p']}

adj_matrix = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0]]


path, expanded = dfs_stack(graph1,'s','g',[])
output = [char for char in path]
print("\nThe path of directed graph 2 through DFS stack with vertex list is : " + "->".join(output))
print("The states expanded with vertex list are:")
print(expanded)

path_AM, expanded_AM = dfs_stack_matrix(adj_matrix,'s','g',[])
output = [char for char in path_AM]
print("\nThe path of directed graph 2 through DFS stack with adjacency matrix : " + "->".join(output))
print("The states expanded with adjacency matrix are:")
print(expanded_AM)