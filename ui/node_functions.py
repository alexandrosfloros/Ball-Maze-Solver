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

### generates list of path intervals between nodes

def get_path_intervals(nodes):

    intervals = []

    for n, node in enumerate(nodes):
        if n == 0:
            intervals.append(0.0)
        else:
            intervals.append(math.dist(node, nodes[n - 1]))

    return intervals

### generates list of path distances to each node

def get_path_distances(nodes):

    intervals = get_path_intervals(nodes)[1:] # removes interval of zero length
    distances = [0.0]

    for n, interval in enumerate(intervals):
        distances.append(interval + distances[n])

    return distances

### generates list of path percentages to each node

def get_path_percentages(nodes):

    nodes_length = len(nodes)
    path_distances = get_path_distances(nodes)
    path_length = sum(get_path_intervals(nodes))

    return [path_distances[n] / path_length for n in range(nodes_length)]

print("Intervals:", get_path_intervals(nodes))
print("Distances:", get_path_distances(nodes))
print("Percentages:", get_path_percentages(nodes))