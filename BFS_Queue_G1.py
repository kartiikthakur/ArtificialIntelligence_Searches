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


path, expanded = BFS(graph1,'s','g')
output = [char for char in path]
print("\nThe path of directed graph 2 through BFS Queue with vertex is : " + "->".join(output))
print("The states expanded are:")
print(expanded)


path_AM, expanded_AM = BFS_Matrix(adj_matrix,'s','g',[])
output1 = [char for char in path_AM]
print("\nThe path of directed graph 2 through BFS Queue with adjacency matrix : " + "->".join(output1))
print("The states expanded with adjacency matrix are:")
print(expanded_AM)