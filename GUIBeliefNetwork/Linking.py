import  math,numpy

#
class Vertex:
    # a constructor to initialize the class
    def __init__(self, node):
        # this gives the node a number
        self.id = node
        # a dictionary like a map in JAVA which stores all adjacent nodes
        self.adjacent = {}

    def __str__(self):
        return str([x.id for x in self.adjacent])

    def check_neighbor_existed(self,node):

        if node in self.adjacent:
            return True
        else:
            return False

    def add_neighbor(self, neighbor, weight=0):

        self.adjacent[neighbor] = weight

    def delete_neighbor(self, neighbor):
        self.adjacent.pop(neighbor)
    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        # dictionary which stores all the vertex
        self.vert_dict = {}
        # the number of vertices increments as nodes are connected
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def delete_vertex(self,node):
        self.num_vertices -=1
        for n in self.vert_dict:
            if self.check_edge_existed(n,node):
                self.vert_dict[n].delete_neighbor(self.vert_dict[node])
        self.vert_dict.pop(node)

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost):
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)


    def delete_edge(self,frm,to):
        self.vert_dict[frm].delete_neighbor(self.vert_dict[to])


    def check_edge_existed(self,frm,to):
        return self.vert_dict[frm].check_neighbor_existed(self.vert_dict[to])

    def get_vertices(self):
        return self.vert_dict.keys()
