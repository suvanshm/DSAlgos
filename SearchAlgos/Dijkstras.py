from DataStructures.Graph import Vertex, Graph
from DataStructures.Heap import MinHeap
from math import inf
from heapq import heappop, heappush


# Home made implementation
def dijkstras(graph, start):
    distances = {}
    for vertex in graph.graph_dict.keys():
        distances[vertex] = inf
    distances[start] = 0
    explore = MinHeap()
    explore.add([0, start])
    while explore:
        try:
            distance, current = explore.get_min()
        except TypeError:
            break
        currentvertex = graph.graph_dict[current]
        neighbours = currentvertex.get_neighbours()
        for neighbour, weight in neighbours:
            newdistance = distance + weight
            if newdistance < distances[neighbour]:
                distances[neighbour] = newdistance
                explore.add([newdistance, neighbour])
    return distances


# Implementation using heapq
def dijkstras2(graph, start):
    distances = {}
    for vertex in graph.graph_dict.keys():
        distances[vertex] = inf
    distances[start] = 0
    explore = [(0, start)]
    while explore:
        distance, current = heappop(explore)
        currentvertex = graph.graph_dict[current]
        neighbours = currentvertex.get_neighbours()
        for neighbour, weight in neighbours:
            newdistance = distance + weight
            if newdistance < distances[neighbour]:
                distances[neighbour] = newdistance
                heappush(explore, (newdistance, neighbour))
    return distances


# Modified dijkstras using a target value
def dijkstras3(graph, start, target):
    paths_and_distances = {}
    for vertex in graph.graph_dict.keys():
        paths_and_distances[vertex] = [inf, [start]]
    paths_and_distances[start][0] = 0
    explore = [(0, start)]
    while explore:
        distance, current = heappop(explore)
        currentvertex = graph.graph_dict[current]
        neighbours = currentvertex.get_neighbours()
        for neighbour, weight in neighbours:
            newdistance = distance + weight
            newpath = paths_and_distances[current][1] + [neighbour]
            if newdistance < paths_and_distances[neighbour][0]:
                paths_and_distances[neighbour][0] = newdistance
                paths_and_distances[neighbour][1] = newpath
                heappush(explore, (newdistance, neighbour))
    return paths_and_distances[target]



#Testing
delhi = Vertex("Delhi")
mumbai = Vertex("Mumbai")
chennai = Vertex("Chennai")
kolkata = Vertex("Kolkata")
srinagar = Vertex("Srinagar")
imphal = Vertex("Imphal")
surat = Vertex("Surat")
bhopal = Vertex("Bhopal")
jaipur = Vertex("Jaipur")
india = Graph()
india.add_vertex(delhi)
india.add_vertex(mumbai)
india.add_vertex(chennai)
india.add_vertex(kolkata)
india.add_vertex(srinagar)
india.add_vertex(imphal)
india.add_vertex(surat)
india.add_vertex(bhopal)
india.add_vertex(jaipur)
india.add_edge(mumbai, chennai, 1.5)
india.add_edge(mumbai, kolkata, 2.5)
india.add_edge(mumbai, delhi, 2)
india.add_edge(delhi, kolkata, 2.5)
india.add_edge(delhi, chennai, 3)
india.add_edge(chennai, kolkata, 2.5)
india.add_edge(mumbai, surat, 0.5)
india.add_edge(delhi, srinagar, 1.5)
india.add_edge(kolkata, imphal, 1)
india.add_edge(bhopal, jaipur, 1.5)

print(dijkstras3(india, "Surat", "Srinagar"))
