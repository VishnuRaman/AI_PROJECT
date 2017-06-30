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
    ##adds a connection to the given neighbor.  It can also be used to set up the cost again
    #input: node needed to be add a connection to
    def add_neighbor(self, neighbor, weight=1):

        self.adjacent[neighbor] = weight
    ##Delete the connection
    #input: node needed to be delete the connection
    def delete_neighbor(self, neighbor):
        self.adjacent.pop(neighbor)
    ##return the list of nodes that connected to itself
    #output: list
    def get_connections(self):
        temp=[i for i in self.adjacent.keys()]
        temp.sort()
        return temp
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
        self.heuristic = {}
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
        self.heuristic[node]=0#(default value = 0)
        return new_vertex
    ##delete a node and every connection with it
    #input: node id
    def delete_vertex(self,node):
        self.num_vertices -=1
        for n in self.vert_dict:#n is the key in that dict
            if self.check_edge_existed(n,node):
                self.vert_dict[n].delete_neighbor(node)
        self.vert_dict.pop(node)
        self.heuristic.pop(node)
    ##get the node object
    #input: node id
    #output: node object
    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None
    ##add a linking. It can also be used to set up the cost again
    #input: from 'node id' to 'node id', and the 'cost' of the linking
    def add_edge(self, frm, to, cost=1):
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
        temp=[n for n in self.vert_dict.keys()]
        temp.sort()
        return temp

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
    #output: all the names as a list [name1.pkl, name2.pkl, ...]
    def fileNames(self):
        temp=[]
        for i in os.listdir(os.getcwd()):
            if '.pkl' in i:
                temp.append(i)
        return temp
    ##allows user to set the heuristic manually within graph structure. If you need the dictionary of Heuristic, call Graph.heustic
    #input: node id, the value of the new heuristic
    def setManualHeuristic(self,node,value):
        if node in self.vert_dict:
            self.heuristic[node]=value

##Grid is the object which can be used to manage vertex. There is a dictionary called 'grid_dict' storing the unit grid id as the key and the vertex object as the value.
class Grid:
    ##Take every unit grid as a vertex object and store them into 'grid_dict'. The grids are numbered from left to right, top to bottom, 0 to x*y-1
    #The default connection is full connected. Default weight of connection is 1.
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
    #input: two unit grid
    def setWall(self,id1,id2):
        self.grid_dict[id1].delete_neighbor(id2)
        self.grid_dict[id2].delete_neighbor(id1)
    ##break the wall between two unit grid.
    #input: two unit grid
    def breakWall(self,id1,id2):
        self.grid_dict[id1].add_neighbor(id2,self.grid_weight[id2])
        self.grid_dict[id2].add_neighbor(id1,self.grid_weight[id1])

    ##this is a method finding the physical  neighbors of a unit grid in a x*y grid. The physical neighbor won't be changed by wall
    #input: a unit grid id
    def physicalNeighbor(self,id):
        phycialNeighbor=[]
        if id>self.x-1:#not on the first row
            upperGrid=id-self.x
            phycialNeighbor.append(upperGrid)
        if id<self.x*(self.y-1):#not on the last row
            underGrid=id+self.x
            phycialNeighbor.append(underGrid)
        if id%self.x !=0:#if not on the leftest column
            leftGrid=id-1
            phycialNeighbor.append(leftGrid)
        if id%self.x !=self.x-1:#if not on the rightest column
            rightGrig=id+1
            phycialNeighbor.append(rightGrig)
        return phycialNeighbor
    ##set the unit grid as an obstacle, means each edge of it becomes a wall
    #input: a unit grid id
    def setObstacle(self,id):
        for n in self.physicalNeighbor(id):
            self.setWall(id,n)
    ##undo setObstacle
    #input: a unit grid id
    def removeObstacle(self,id):
        for n in self.physicalNeighbor(id):
            self.breakWall(id,n)
    ##set the cost of beging connected for other unit grids.
    #input: the id of itself. The weight
    def setGridWeight(self,id,weight):
        self.grid_weight[id]=weight
        for n in self.physicalNeighbor(id):
            if id in self.grid_dict[n].adjacent.keys():
                self.grid_dict[n].add_neighbor(id,weight)
    ## generate the Manhattan Distance for every unit grid to the goal
    #input: the goal
    #output: a dictionary. grid id as the key, Manhattan Distance as the value.
    def getManhattanDist(self,goal):
        grid_manhattan={}
        (yCoordinate,xCoordinate)=divmod(goal,self.x)#yCoordinate is the quotient, xCoordinate is the reminder
        for j in range(self.y):
            for i in range(self.x):
                id=self.x*j+i
                grid_manhattan[id]=abs(i-xCoordinate)+abs(j-yCoordinate)

        return grid_manhattan

    ##save the current vert_dict with given fileName
    #input: fileName as a string
    def saveFile(self,fileName):
        newDict=self.grid_dict
        output = open(fileName+'.pkl', 'wb')
        pickle.dump(newDict, output)
        output.close()

    ##load the stored vert_dict with having the name fileName
    #input: fileName as a string
    #output: dictionary
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