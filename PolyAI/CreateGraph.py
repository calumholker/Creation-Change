import numpy as np

coords = [[0,0], [0,1], [0,2], [1,2]]
N=4

def get_distance(coord1, coord2):
    coord1 = np.asarray(coord1)
    coord2 = np.asarray(coord2)
    return np.linalg.norm(coord1-coord2)

def get_graph(N, coords, weight_Func):
    graph = {}
    for i in range(N):
        graph[str(i)] = {}

    for i, coord1 in enumerate(coords):
        for j, coord2 in enumerate(coords):
            if i != j:
                if str(j) not in graph[str(i)]:
                    weight = weight_Func(coord1, coord2)
                    graph[str(i)][str(j)] = weight
                    graph[str(j)][str(i)] = weight
    return graph

print(get_graph(N, coords, get_distance))