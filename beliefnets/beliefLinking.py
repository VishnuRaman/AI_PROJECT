import  math,numpy,pickle,os

##Vertex is a basic object representing the conception of node. The id is the identity of the node,
# and the dictionary called 'adjacent' is used to store the id of the nodes which it is connecting to. The id as the key, while the weight of the connection as the value.
class Vertex:
    ## a constructor to initialize the class
    def __init__(self, id):
        # this gives the node a number
        self.id = id
        self.heuristic=0#default value=0
        self.utility=0#default value=0
        self.probability=1#default value=1
        # a dictionary like a map in JAVA which stores all adjacent nodes
        self.adjacent = {}
        self.probabilityTable={}

    def __iter__(self):
        return iter(self.adjacent.keys())

    ##checks if the given node is already connected
    #input: @arg1 node needed to be check
    #output: Boolean
    def check_neighbor_existed(self,id):

        if id in self.adjacent:
            return True
        else:
            return False
    ##adds a connection to the given neighbor.
    def add_neighbor(self, id):
        self.adjacent[id]
    ##Delete the connection
    #input:@arg1 node needed to be delete the connection
    def delete_neighbor(self, id):
        self.adjacent.pop(id)
    ##return the list of nodes that connected to itself
    #output: list
    def get_connections(self):
        temp=[i for i in self.adjacent.keys()]
        temp=sorted(temp,key=lambda x: str(x))#use lamda expression to sort them as string
        return temp#but when output, they are stll int
    ##get the id of itself
    #output: id number
    def get_id(self):
        return self.id

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
    #input:@arg1  node id of the node needed to be create
    #output: the node object just be created
    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
    ##just like add_vertex, this method create a new action object.
    #input:@arg1 id of the action. ie 'a0', 'a1' ...
    def add_objEdge(self,actionId):
        new_edge= Edge(actionId)
        self.vert_dict[actionId]=new_edge
    ##this method will delete the action object from vert_dict and remove all the related connection
    #input: @arg1 action id
    def delete_objEdge(self,actionId):
        for n in self.vert_dict:
            if type(self.vert_dict[n]) is Vertex and actionId in self.vert_dict[n].adjacent:#delete all connections from vertex
                self.vert_dict[n].adjacent.pop(actionId)
        self.vert_dict.pop(actionId)#delete itself from vert_dict
    ##just like add_edge, but it can only be used to add the connection between node(as child) and action(as parent)
    #input: @arg1 action id, @arg2 the chance of the vertex, @arg3 the vertex object
    def add_objEdge_vert_connection(self,edgeId,nodeId):
        self.vert_dict[edgeId].add_neighbor(nodeId)
    def delete_objEdge_vert_connection(self,edgeId,nodeId):
        self.vert_dict[edgeId].delete_neighbor(nodeId)
    ##delete a node and every connection with it
    #input:@arg1 node id
    def delete_vertex(self,node):
        self.num_vertices -=1
        for n in self.vert_dict:#n is the key in that dict
            if self.check_edge_existed(n,node):
                self.get_vertex(n).delete_neighbor(node)
        self.vert_dict.pop(node)
    ##get the node object
    #input:@arg1  node id
    #output: node object
    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None
    ##add a linking. It can also be used to set up the cost again.
    #input:@arg1  from 'node id', @arg2 to 'node id',
    def add_edge(self, frm, to):
        self.vert_dict[frm].add_neighbor(to)
    ##delete a linking
    #input:@arg1  from 'node id' to 'node id'
    def delete_edge(self,frm,to):
        self.vert_dict[frm].delete_neighbor(to)
    ##check if the linking is existed
    #input:@arg1  from 'node id' to 'node id'
    #output: Boolean
    def check_edge_existed(self,frm,to):
        return self.vert_dict[frm].check_neighbor_existed(to)
    ##get the list of vertex that already created
    #output: list
    def get_vertices(self):
        temp=[n for n in self.vert_dict.keys()]
        temp=sorted(temp,key=lambda x: str(x))
        return temp


