import numpy as np
import fileinput

def get_input():
    '''
    Fetch nodes, number of nodes and the coordinates of zearth from the input file
    '''
    lines = [line.rstrip('\n') for line in (fileinput.input())]

    num_nodes = int(lines[1]) # Get number of nodes and validate value
    if (num_nodes < 1) or (num_nodes > 2000):
        raise Exception('Invalid number of stations')
    earth = [0.0,0.0,0.0] # Earth coordinates
    zearth = to_coords(lines[0])
    nodes = []
    nodes.append(earth)
    nodes.append(zearth)

    for i in range(num_nodes):
        coord = to_coords(lines[i+2]) # Get the remainding coordinates
        nodes.append(coord)

    return nodes, num_nodes+2 # Output list of nodes and the number of nodes (including earth and zearth)

def to_coords(line):
    '''
    Extracts coordinates from a string fetched from the .txt file
    '''
    coords = []
    for num in line.split():
        num = float(num)
        if (num < -10000.0) or (num > 10000.0): # Validates coordinate values
            raise Exception('Invalid coordinate value')
        coords.append(num)
    return coords


def euclidean_distance(coord1, coord2):
    '''
    Calculates the euclidean distance between two coordinates
    '''
    coord1 = np.asarray(coord1)
    coord2 = np.asarray(coord2)
    return np.linalg.norm(coord1-coord2)

def get_graph(num_nodes, nodes, weight_Func):
    '''
    Creates a fully connected graph in dictionary form for the nodes. Each edge has a weight value determined by weight_Func
    '''
    graph = {} # Creates empty graph with the required number of nodes with no edges
    for i in range(num_nodes):
        graph[str(i)] = {} # Each node is labeled with a number e.g: zearth = '1'

    # Adds each edge to the fully connected graph with weight values assigned
    for i, node1 in enumerate(nodes):
        for j, node2 in enumerate(nodes):
            if i != j:
                if str(j) not in graph[str(i)]: # Assuring each weight is only calculated once
                    weight = weight_Func(node1, node2)
                    graph[str(i)][str(j)] = weight
                    graph[str(j)][str(i)] = weight
    return graph

def find_max_distance(graph, start, goal):
    '''
    Uses Dijkstra's algorithm to find the path with the minimum maximum distance between the start node and the end node.
    Instead of taking the total weight to get from the start to each node, it takes the maximum of the weights along the path.
    '''
    max_distance = {}
    unseenNodes = graph
    infinity = float("inf")
    for node in unseenNodes: # Initiates the minimum maximum distance for each node to be infinity
        max_distance[node] = infinity
    max_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes: # Finding the minimum weighted node so far
            if minNode is None: # Base case
                minNode = node
            elif max_distance[node] < max_distance[minNode]:
                minNode = node
        
        for childNode, weight in graph[minNode].items():
            if max(weight, max_distance[minNode]) < max_distance[childNode]: # Takes maximum of weights along path
                max_distance[childNode] = max(weight, max_distance[minNode])
        unseenNodes.pop(minNode) # Breaks loop when finished
    
    return max_distance[goal]

if __name__ == "__main__":
    nodes, num_nodes = get_input() # Retrieves data
    earth = '0'
    zearth = '1'
    graph = get_graph(num_nodes, nodes, euclidean_distance) # Get fully connected graph for all nodes
    result = find_max_distance(graph, earth, zearth) # Get the maximum distance for the best path
    print(result)