def BFS(graph, start, end):
    visited = set()
    expanded = []
    queue = [start]

    while queue:
        path = queue.pop(0)
        current = path[-1]
        if current not in expanded:
            expanded.append(path[-1])

        if current not in visited:
            visited.add(current)

        if current == end:
            return path, expanded

        neighbours = graph[current]
        for j in neighbours:
            if j not in visited:
                appends = path + j
                queue.append(appends)


maps = {'a':0, 'b': 1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'p':8, 'q':9,  'r':10, 's':11 }
def BFS_Matrix(graph, start, goal, list):
    visited = set()
    expanded = []
    queue = [start]

    while queue:
        path = queue.pop(0)
        current = path[-1]

        if current not in expanded:
            expanded.append(path[-1])

        if current not in visited:
            visited.add(current)

        if current == goal:
            return path, expanded

        length = len(graph[maps[current]])
        for neighbor in range(length):
            if neighbor not in visited and graph[maps[current]][neighbor] == 1:
                    j = [k for k,v in maps.items() if v == neighbor]
                    if j[0] not in visited:
                        appends = path + j[0]
                        queue.append(appends)


graph2 = {
    'a': [],
    'b': ['a'],
    'c': [],
    'd': ['b', 'c', 'e'],
    'e': ['h', 'r'],
    'f': ['c', 'g'],
    'g': [],
    'h': ['p', 'q'],
    'p': ['q'],
    'q': [],
    'r': ['f'],
    's': ['d', 'e', 'p']}

Adj_matrix=[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0]]


path, expanded = BFS(graph2,'s','g')
output = [char for char in path]
print("\nThe path of graph 2 through BFS Queue with vertex list is : " + "->".join(output) + "\n")
print("The states expanded with vertex list are:")
print(expanded)

path_AM, expanded_AM = BFS_Matrix(Adj_matrix,'s','g',[])
output1 = [char for char in path]
print("\nThe path of graph 2 through BFS Queue with adjacency matrix is : " + "->".join(output1) + "\n")
print("The states expanded with adjacency matrix are:")
print(expanded)