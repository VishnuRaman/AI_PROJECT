import  math,numpy,pickle,os

##Vertex is a basic object representing the conception of node. The id is the identity of the node,
# and the dictionary called 'adjacent' is used to store the id of the nodes which it is connecting to. The id as the key, while the weight of the connection as the value.
class Vertex:
    ## a constructor to initialize the class
    def __init__(self, id):
        # this gives the node a number
        self.id = id
        self.heuristic=0#default value=0
        self.utility=None#default value=None
        self.probability=0.5#default value=0.5, for belief net(prior probability) and Markov(initial probability) algorithm
        self.adjacent = {}
        self.probabilityTable={}#distribution probability table
        self.reward=0

    def __iter__(self):#makes vertex object iterable
        return iter(self.adjacent.keys())

    ##checks if the given node is already connected
    #input: @arg1 node needed to be check
    #output: Boolean
    def check_connectingTo(self,id):

        if id in self.adjacent:
            return True
        else:
            return False
    ##adds a connection to the given neighbor.  It can also be used to set up the cost again
    #input:@arg1  node needed to be add a connection to, @arg2 the weight of the connection
    def add_neighbor(self, id, weight):
        self.adjacent[id] = weight
    ##Delete the connection
    #input:@arg1 node needed to be delete the connection
    def delete_neighbor(self, id):
        self.adjacent.pop(id)
    ##return the list of nodes that it connects to
    #output: list
    def get_connections(self):
        temp=list(self.adjacent)
        temp=sorted(temp,key=lambda x: str(x))#use lamda expression to sort them as string
        return temp#but when output, they are stll int
    ##get the id of itself
    #output: id number
    def get_id(self):
        return self.id
    ##get the weight of a neighbor
    #input: @arg1 node id
    #output: weight
    def get_weight(self, id):
        return self.adjacent[id]

##Edge is the object contains several probabilities and corresponding vertex object. It's a bridge between vertexs.
class Edge:
    def __init__(self,id):
        self.id=id
        self.neighbor={}
    ##connect this action to a vertex (with chance)
    #input: @arg1 chance, @arg2 vertex id
    def add_neighbor(self,id,probability):
        self.neighbor[id]=probability
    def delete_neighbor(self,id):
        self.neighbor.pop(id)



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
    def add_objEdge_vert_connection(self,edgeId,nodeId,probability):
        self.vert_dict[edgeId].add_neighbor(nodeId,probability)
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
    #input:@arg1  from 'node id', @arg2 to 'node id',  @arg3  the 'cost' of the linking(searching).  the 'probability' of the linking(exMinimax, markov)
    def add_edge(self, frm, to, cost=1):
        self.vert_dict[frm].add_neighbor(to, cost)
    ##delete a linking
    #input:@arg1  from 'node id' to 'node id'
    def delete_edge(self,frm,to):
        self.vert_dict[frm].delete_neighbor(to)
    ##check if the linking is existed
    #input:@arg1  from 'node id' to 'node id'
    #output: Boolean
    def check_edge_existed(self,frm,to):
        return self.vert_dict[frm].check_connectingTo(to)
    ##get the list of vertex that already created
    #output: list
    def get_vertices(self):
        temp=list(self.vert_dict)
        temp=sorted(temp,key=lambda x: str(x))
        return temp

    #reset all heuristic to 0
    def resetAllHeuristic(self):
        for node in self.vert_dict:
            self.get_vertex(node).heuristic=0
    ##reset all utility to default
    def resetAllUtility(self):
        for node in self.vert_dict:
            self.get_vertex(node).utility=0


##Grid is the object which can be used to manage vertex. There is a dictionary called 'grid_dict' storing the unit grid id as the key and the vertex object as the value.
class Grid:
    ##Take every unit grid as a vertex object and store them into 'grid_dict'. The grids are numbered from left to right, top to bottom, 0 to x*y-1
    #The default connection is full connected. Default weight of connection is 1.
    #input:@arg1 columns, @arg2 rows
    def __init__(self,x,y):# for a x*y grid
        self.grid_dict={}#stores the vertex objects as the unit grids
        self.grid_weight={}#stroes the weight corresponding to the vertex id
        self.x=x
        self.y=y

        for j in range(y):# Create vertexs and store in  grid_dict
            for i in range(x):
                id=x*j+i#number the grids from left to right, top to bottom, 0 to x*y-1
                new_vertex = Vertex(id)
                self.grid_dict[id] = new_vertex
                self.grid_weight[id] = 1 #default cost of every unit grid is 1
        for j in range(y):# Generate the default connection of each unit grid in the x*y grid. The default weight of connection is 1
            for i in range(x):
                id=x*j+i
                if i==0:#generate X-asix connection
                    self.grid_dict[id].add_neighbor(id+1)#id+1 is the node right to itself.
                elif i==x-1:
                    self.grid_dict[id].add_neighbor(id-1)#id-1 is the node left to itself.
                else:
                    self.grid_dict[id].add_neighbor(id-1)#id-1 is the node left to itself.
                    self.grid_dict[id].add_neighbor(id+1)#id+1 is the node right to itself.
                if j==0:#generate Y-axis connection
                    self.grid_dict[id].add_neighbor(id+x)#id+x is the node under itself.
                elif j==y-1:
                    self.grid_dict[id].add_neighbor(id-x)#id-x is the upper node.
                else:
                    self.grid_dict[id].add_neighbor(id-x)#id-x is the upper node.
                    self.grid_dict[id].add_neighbor(id+x)#id+x is the node under itself.


    ##set a wall between two unit grid
    #input:@arg1  two unit grid
    def setWall(self,id1,id2):
        self.grid_dict[id1].delete_neighbor(id2)
        self.grid_dict[id2].delete_neighbor(id1)
    ##break the wall between two unit grid.
    #input:@arg1  two unit grid
    def breakWall(self,id1,id2):
        self.grid_dict[id1].add_neighbor(id2,self.grid_weight[id2])
        self.grid_dict[id2].add_neighbor(id1,self.grid_weight[id1])

    ##this is a method finding the physical  neighbors of a unit grid in a x*y grid. The physical neighbor won't be changed by wall
    #input:@arg1  a unit grid id
    def physicalNeighbor(self,id):
        phycialNeighbor={}
        if id>self.x-1:#not on the first row
            upperCell=id-self.x
            phycialNeighbor['upperCell']=upperCell
        if id<self.x*(self.y-1):#not on the last row
            underCell=id+self.x
            phycialNeighbor['underCell']=underCell
        if id%self.x !=0:#if not on the leftest column
            leftCell=id-1
            phycialNeighbor['leftCell']=leftCell
        if id%self.x !=self.x-1:#if not on the rightest column
            rightCell=id+1
            phycialNeighbor['rightCell']=rightCell
        return phycialNeighbor
    ##set the unit grid as an obstacle, means each edge of it becomes a wall
    #input:@arg1  a unit grid id
    def setObstacle(self,id):
        phycialNeighbor=self.physicalNeighbor(id)
        for n in phycialNeighbor:
            self.setWall(id,phycialNeighbor[n])
    ##undo setObstacle
    #input:@arg1  a unit grid id
    def removeObstacle(self,id):
        phycialNeighbor=self.physicalNeighbor(id)
        for n in phycialNeighbor:
            self.breakWall(id,phycialNeighbor[n])
    ##set the cost of beging connected by other unit grids.
    #input:@arg1  the id of itself, @arg2  The weight
    def setGridWeight(self,id,weight):
        self.grid_weight[id]=weight
        phycialNeighbor=self.physicalNeighbor(id)
        for n in phycialNeighbor:
            if id in self.grid_dict[phycialNeighbor[n]].adjacent.keys():
                self.grid_dict[phycialNeighbor[n]].add_neighbor(id,weight)#add_neighbor can also be used to reset the value
    ## generate the Manhattan Distance for every unit grid to the goal
    #input: @arg1 the goal
    def setManhattanDist(self,goal):
        (yCoordinate,xCoordinate)=divmod(goal,self.x)#yCoordinate is the quotient, xCoordinate is the reminder
        for j in range(self.y):
            for i in range(self.x):
                id=self.x*j+i
                self.grid_dict[id].heuristic=abs(i-xCoordinate)+abs(j-yCoordinate)

    ##reset all utility to default
    def resetAllUtility(self):
        for node in self.grid_dict:
            self.grid_dict[node].utility=0