from DataStructures.Graph import Vertex, Graph


# bfs
# input graph, start and target
# create visited set
# create queue
# while queue:
# pop off item of queue into current vertex and path
# add current vertex to visited
# loop neighbours of current vertex
# if neighbour not in visited
# and if current vertex is target return path + neighbor
# else append neighbor and updated path to queue

def bfs(graph, start, target):
    visited = set()
    queue = [[start, [start]]]
    while queue:
        current, path = queue.pop(0)
        visited.add(current)
        currentvertex = graph.graph_dict[current]
        neighbours = currentvertex.get_edges()
        for neighbour in neighbours:
            if neighbour not in visited:
                if neighbour == target:
                    return path + [neighbour]
                else:
                    queue.append([neighbour, path + [neighbour]])


# dfs
# input graph, start, target, visit default empty list
# add start to visit
# if start = target return visit
# for neighbor of current
# if neighbor not in visit call recursively
# if recursive call path exists, return that

def dfs(graph, start, target, visit=[]):
    visit.append(start)
    if start == target:
        return visit
    currentvertex = graph.graph_dict[start]
    neighbours = currentvertex.get_edges()
    for neighbour in neighbours:
        if neighbour not in visit:
            path = dfs(graph, neighbour, target, visit)
            if path:
                return path



#Testing
muwci = Graph()
w1 = Vertex("Wada 1")
w2 = Vertex("Wada 2")
w3 = Vertex("Wada 3")
w4 = Vertex("Wada 4")
w5 = Vertex("Wada 5")
aq = Vertex("AQ")
caf = Vertex("Caf")
treehouse = Vertex("Treehouse")
oc = Vertex("OC")
pool = Vertex("Pool")
bioreserve = Vertex("Bioreserve")
muwci.add_vertex(w1)
muwci.add_vertex(w2)
muwci.add_vertex(w3)
muwci.add_vertex(w4)
muwci.add_vertex(w5)
muwci.add_vertex(aq)
muwci.add_vertex(caf)
muwci.add_vertex(treehouse)
muwci.add_vertex(oc)
muwci.add_vertex(bioreserve)
muwci.add_vertex(pool)
muwci.add_edge(w1, w2)
muwci.add_edge(w1, w3)
muwci.add_edge(w2, w4)
muwci.add_edge(w2, caf)
muwci.add_edge(caf, aq)
muwci.add_edge(treehouse, w3)
muwci.add_edge(w2, oc)
muwci.add_edge(caf, bioreserve)
muwci.add_edge(aq, bioreserve)
muwci.add_edge(w3, pool)
muwci.add_edge(w4, pool)
print(w2.get_edges())

print(dfs(muwci, "Wada 2", "Bioreserve"))

