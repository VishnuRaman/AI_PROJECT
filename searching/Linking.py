import  math,numpy,pickle,os

##Vertex is a basic object representing the conception of node. The id is the identity of the node,
# and the dictionary called 'adjacent' is used to store the id of the nodes which it is connecting to. The id as the key, while the weight of the connection as the value.
class Vertex:
    ## a constructor to initialize the class
    def __init__(self, node):
        # this gives the node a number
        self.id = node
        # a dictionary like a map in JAVA which stores all adjacent nodes
        self.adjacent = {}

    def __iter__(self):######
        return iter(self.adjacent.keys())

    ##checks if the given node is already connected
    #input: node needed to be check
    #output: Boolean
    def check_neighbor_existed(self,node):

        if node in self.adjacent:
            return True
        else:
            return False
    ##adds a neighbour node into the adjacent one - ie adjacent becomes the neighbour
    #input: node needed to be add
    def add_neighbor(self, neighbor, weight=1):

        self.adjacent[neighbor] = weight
    ##Delete the node
    #input: node needed to be delete
    def delete_neighbor(self, neighbor):
        self.adjacent.pop(neighbor)
    ##return the list of nodes that connected to itself
    #output: list
    def get_connections(self):
        return self.adjacent.keys()
    ##get the id of itself
    #output: id number
    def get_id(self):
        return self.id
    ##get the weight of a neighbor
    #input: node id
    #output: weight
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

##Graph is the object which can be used to manage vertex. There is a dictionary called 'ver_dict' storing the node id as the key and the vertex object as the value.
#Read through the vert_dict we can know how many nodes are in a graph, and read through each vertex we can know the connection between them.
class Graph:
    def __init__(self):
        # dictionary which stores all the vertex
        self.vert_dict = {}
        # the number of vertices increments as nodes are connected
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())
    ##add a new vertex
    #input: node id of the node needed to be create
    #output: the node object just be created
    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex
    ##delete a node and every connection with it
    #input: node id
    def delete_vertex(self,node):
        self.num_vertices -=1
        for n in self.vert_dict:#n is the key in that dict
            if self.check_edge_existed(n,node):
                self.vert_dict[n].delete_neighbor(node)
        self.vert_dict.pop(node)
    ##get the node object
    #input: node id
    #output: node object
    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None
    ##add a linking
    #input: from 'node id' to 'node id', and the 'cost' of the linking
    def add_edge(self, frm, to, cost):
        self.vert_dict[frm].add_neighbor(to, cost)
    ##delete a linking
    #input: from 'node id' to 'node id'
    def delete_edge(self,frm,to):
        self.vert_dict[frm].delete_neighbor(to)
    ##check if the linking is existed
    #input: from 'node id' to 'node id'
    #output: Boolean
    def check_edge_existed(self,frm,to):
        return self.vert_dict[frm].check_neighbor_existed(to)
    ##get the list of vertex that already created
    #output: list
    def get_vertices(self):
        return [n for n in self.vert_dict.keys()]

    ##save the current vert_dict with given fileName
    #input: fileName as a string
    def saveFile(self,fileName):
        newDict=self.vert_dict
        output = open(fileName+'.pkl', 'wb')
        pickle.dump(newDict, output)
        output.close()

    ##load the stored vert_dict with having the name fileName
    #input: fileName as a string
    #output: vert_dict
    def loadFile(self,fileName):
        # read python dict back from the file
        file = open(fileName+'.pkl', 'rb')
        dict = pickle.load(file)
        file.close()
        return dict

    ##see all the .pkl files name
    #output: all the names as a list
    def fileNames(self):
        temp=[]
        for i in os.listdir(os.getcwd()):
            if '.pkl' in i:
                temp.append(i)
        return temp


# g=Graph()
# for i in range(7):
#     g.add_vertex(i)
# g.add_edge(0,1,1)
# g.add_edge(0,2,1)
# g.add_edge(1,3,1)
# g.add_edge(1,4,1)
# g.add_edge(2,5,1)
# g.add_edge(2,6,1)
# g.saveFile('junk')
# print(g.fileNames())
# dict=g.loadFile('junk')
# for v in dict:#####
#     print(str(dict[v].get_id())+' is connected to '+str([g for g in dict[v]]))
