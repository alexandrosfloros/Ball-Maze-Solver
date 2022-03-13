import math

### example nodes

nodes = [
    [0.0, 0.0],
    [1.0, 1.0],
    [2.0, 0.0],
    [3.0, 0.0],
    [3.0, 2.0],
    [10.0, 2.0]
]

### generates list of path distances between nodes

def get_path_distances(nodes):

    path_distances = []

    for n, node in enumerate(nodes):
        if n == 0:
            path_distances.append(0.0)
        else:
            path_distances.append(math.dist(node, nodes[n - 1]))

    return path_distances

### generates list of path lengths to each node

def get_path_lengths(nodes):

    path_distances = get_path_distances(nodes)[1:] # removes distance of zero length
    path_lengths = [0.0]

    for n, distance in enumerate(path_distances):
        path_lengths.append(distance + path_lengths[n])

    return path_lengths

### generates list of path length percentages to each node

def get_path_length_percentages(nodes):

    path_lengths = get_path_lengths(nodes)
    total_path_length = sum(get_path_distances(nodes))
    no_of_nodes = len(nodes)

    return [path_lengths[n] * 100 / total_path_length for n in range(no_of_nodes)]

