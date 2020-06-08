from DataStructures.Graph import Vertex, Graph
from heapq import heappush, heappop
from math import inf


def heuristic(start, end):
    # Modify accordingly. I was too lazy to prepare a vertex graph with positional values.
    return 0


def astar(graph, start, target):
    path_and_distance = {}
    for vertex in graph.graph_dict.keys():
        path_and_distance[vertex] = [inf, [start]]
    path_and_distance[start][0] = 0
    explore = [(0, start)]
    while explore and path_and_distance[target][0] == inf:
        distance, current = heappop(explore)
        currentvertex = graph.graph_dict[current]
        neighbours = currentvertex.get_neighbours()
        for neighbour, weight in neighbours:
            newdistance = distance + weight + heuristic(neighbour, target)
            newpath = path_and_distance[current][1] + [neighbour]
            if newdistance < path_and_distance[neighbour][0]:
                path_and_distance[neighbour][0] = newdistance
                path_and_distance[neighbour][1] = newpath
                heappush(explore, (newdistance, neighbour))
    return path_and_distance[target]

