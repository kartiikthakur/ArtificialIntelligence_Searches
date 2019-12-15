def mapss(o):
    j = [k for k, v in maps.items() if v == o]
    return j[0]

def dfs_recursive(graph, start, end, path, expanded = []):

    if start not in path:
        path = path + [start]

    if start not in expanded:
        expanded.append(start)

    if start == end:
        return expanded, path

    neighbors = graph[start]
    for node in neighbors:
        if node not in expanded:
            expanded.append(node)

        if node not in path:
            output = dfs_recursive(graph, node, end, path, expanded)
            if output is not None:
                return output





maps = {0:'a', 1: 'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'p', 9:'q', 10: 'r', 11:'s' }

def dfs_matrix(graph,star,end, path, expanded=[]):
    start = mapss(star)
    goal = mapss(end)

    if start not in path:
        path = path + [start]

    if start not in expanded:
        expanded.append(start)

    if start == goal:
        return [maps[x] for x in path], [maps[x] for x in expanded]

    for neighbor in range(len(graph[start])):
        if neighbor not in expanded and graph[start][neighbor] == 1:
            output = dfs_matrix(graph, maps[neighbor], end, path, expanded)
            if output is not None:
                return output



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

path, states = dfs_recursive(graph1,'s','g',[])
print("\nThe path of undirected graph 1 through DFS recursive using Vertex list is : " + "->".join(path))
print("The states expanded in vertex list are:")
print(states)


path_AM, visited_AM = dfs_matrix(adj_matrix, 's','g', [], [])
print("\nThe path of undirected graph 1 through DFS recursive using Adjacency Matrix is : " + "->".join(path_AM))
print("The states expanded in Adjacency Matrix are:")
print(visited_AM)

