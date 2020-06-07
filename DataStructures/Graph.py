class Vertex:

    def __init__(self, value):
        self.value = value
        self.edges = {}

    def add_edge(self, vertex, weight=0):
        self.edges[vertex.value] = weight

    def delete_edge(self, vertex):
        del self.edges[vertex.value]

    def get_edges(self):
        return list(self.edges.keys())


class Graph:

    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        from_vertex.add_edge(to_vertex, weight)
        if not self.directed:
            to_vertex.add_edge(from_vertex, weight)

    def path(self, from_vertex, to_vertex):
        visit = [from_vertex]
        seen = {}
        while len(visit) > 0:
            current = visit.pop(0)
            if current == to_vertex:
                return True
            seen[current] = True
            currentnode = self.graph_dict[current]
            nextnodes = currentnode.get_edges()
            visit += [i for i in nextnodes if i not in seen]
        return False


# Vertex Testing
# delhi = Vertex("Delhi")
# mumbai = Vertex("Mumbai")
# chennai = Vertex("Chennai")
# kolkata = Vertex("Kolkata")
# srinagar = Vertex("Srinagar")
# imphal = Vertex("Imphal")
# surat = Vertex("Surat")
# bhopal = Vertex("Bhopal")
# jaipur = Vertex("Jaipur")
# print(delhi.value)
# delhi.add_edge(mumbai, 1.5)
# delhi.add_edge(chennai, 2)
# print(delhi.get_edges())
# print(mumbai.get_edges())
# print(delhi.edges[mumbai.value])
# delhi.delete_edge(chennai)
# print(delhi.get_edges())

#Graph Testing
# india = Graph()
# india.add_vertex(delhi)
# india.add_vertex(mumbai)
# india.add_vertex(chennai)
# india.add_vertex(kolkata)
# india.add_vertex(srinagar)
# india.add_vertex(imphal)
# india.add_vertex(surat)
# india.add_vertex(bhopal)
# india.add_vertex(jaipur)
# india.add_edge(mumbai, chennai, 1.5)
# india.add_edge(mumbai, kolkata, 2.5)
# india.add_edge(mumbai, delhi, 2)
# india.add_edge(delhi, kolkata, 2.5)
# india.add_edge(delhi, chennai, 3)
# india.add_edge(chennai, kolkata, 2.5)
# india.add_edge(mumbai, surat, 0.5)
# india.add_edge(delhi, srinagar, 1.5)
# india.add_edge(kolkata, imphal, 1)
# india.add_edge(bhopal, jaipur, 1.5)
# print(delhi.get_edges())
# print(mumbai.get_edges())
# print(chennai.get_edges())
# print(kolkata.get_edges())
# print(srinagar.get_edges())
# print(imphal.get_edges())
# print(surat.get_edges())
# print(india.path("Delhi", "Mumbai"))
# print(india.path(delhi.value, srinagar.value))
# print(india.path("Srinagar", "Mumbai"))
# print(india.path("Surat", "Imphal"))
# print(india.path("Chennai", "Chennai"))
# print(india.path("Chennai", "Kochi"))
# print(india.path("Bhopal", "Delhi"))
# print(india.path("Bhopal", "Jaipur"))






