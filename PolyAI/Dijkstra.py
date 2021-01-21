graph = {'s':{'b':2, 'f':3},'b':{'c':2},'c':{'d':2},'d':{'f':2},'f':{}}

def dijkstra(graph, start, goal):
    max_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = float("inf")
    path = []
    for node in unseenNodes:
        max_distance[node] = infinity
    max_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif max_distance[node] < max_distance[minNode]:
                minNode = node
        
        for childNode, weight in graph[minNode].items():
            if max(weight, max_distance[minNode]) < max_distance[childNode]:
                max_distance[childNode] = max(weight, max_distance[minNode])
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)
    
    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0,currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('path not reachable')
            break
    path.insert(0,start)
    if max_distance[goal] != infinity:
        print('Shortest distance is ' + str(max_distance[goal]))
        print('And the path is ' + str(path))

dijkstra(graph, 's', 'f')