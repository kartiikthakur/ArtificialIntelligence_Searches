try:
    import queue
except ImportError:
    import Queue as queue

from queue import PriorityQueue


graph3 = {
    'a': {'b':2,'c':2},
    'b': {'a':2,'d':1},
    'c': {'a':2,'d':8,'f':3},
    'd': {'b':1,'c':8,'e':2,'s':3},
    'e': {'d':2,'h':8,'r':2,'s':9},
    'f': {'c':3,'g':2,'r':2},
    'g': {'f':2},
    'h': {'e':8,'p':4,'q':4},
    'p': {'h':4,'q':15,'s':1},
    'q': {'h':4,'p':15},
    'r': {'e':2,'f':2},
    's': {'d':3,'e':9,'p':1}
}



AM3=     [[0,2,2,0,0,0,0,0,0,0,0,0],
         [2,0,0,1,0,0,0,0,0,0,0,0],
         [2,0,0,8,0,3,0,0,0,0,0,0],
         [0,1,8,0,2,0,0,0,0,0,0,3],
         [0,0,0,2,0,0,0,8,0,0,2,9],
         [0,0,3,0,0,0,2,0,0,0,2,0],
         [0,0,0,0,0,2,0,0,0,0,0,0],
         [0,0,0,0,8,0,0,0,4,4,0,0],
         [0,0,0,0,0,0,0,4,0,15,0,1],
         [0,0,0,0,0,0,0,4,15,0,0,0],
         [0,0,0,0,2,2,0,0,0,0,0,0],
         [0,0,0,3,9,0,0,0,1,0,0,0]]


def UCS(graph, start, goal):
    visited = set()
    expanded=[]
    queue = PriorityQueue()
    queue.put((0, start))



    while queue:
        cost, node = queue.get()
        current = node[-1]
        if current not in visited:
            visited.add(current)
            expanded.append(current)

            if current == goal:
                return node, expanded

            neighbours = graph[current]
            for i in neighbours:
                if i not in visited:
                    total_cost = cost + neighbours[i]
                    queue.put((total_cost, node+i))


maps = {'a':0, 'b': 1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'p':8, 'q':9,  'r':10, 's':11 }
def USC_Matrix(graph,start, goal):
    visited = set()
    expanded = []
    queue = PriorityQueue()
    queue.put((0, start))

    while queue:
        cost, node = queue.get()
        current = node[-1]
        if current not in visited:
            visited.add(current)
            expanded.append(current)

            if current == goal:
                return node, expanded


        length = len(graph[maps[current]])
        for neighbor in range(length):
            if neighbor not in visited and graph[maps[current]][neighbor] >= 1:
                j = [k for k, v in maps.items() if v == neighbor]
                if j[0] not in visited:
                    total_cost = cost + graph[maps[current]][neighbor]
                    queue.put((total_cost, node + j[0]))



path, expanded = UCS(graph3,'s','g')
output = [char for char in path]
print("\nThe path of undirected graph 3 through UCS Priority Queue with vertex list is : " + "->".join(output))
print("The states expanded with vertex list are:")
print(expanded)


path_AM, expanded_AM = USC_Matrix(AM3,'s','g')
output1 = [char for char in path]
print("\nThe path of undirected graph 3 through UCS Priority Queue with adjacency matrix is : " + "->".join(output1))
print("The states expanded with adjacency matrix are:")
print(expanded)

