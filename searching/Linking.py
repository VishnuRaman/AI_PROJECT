import  math,numpy,pickle,os

#
class Vertex:
    # a constructor to initialize the class
    def __init__(self, node):
        # this gives the node a number
        self.id = node
        # a dictionary like a map in JAVA which stores all adjacent nodes
        self.adjacent = {}

    def __iter__(self):######
        return iter(self.adjacent.keys())

    #checks if selected node in the brackets is adjacent to the other node
    def check_neighbor_existed(self,node):

        if node in self.adjacent:
            return True
        else:
            return False
    #adds a neighbour node into the adjacent one - ie adjacent becomes the neighbour
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
        for n in self.vert_dict:#n is the key in that dict
            if self.check_edge_existed(n,node):
                self.vert_dict[n].delete_neighbor(node)
        self.vert_dict.pop(node)


    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None



    def add_edge(self, frm, to, cost):
        self.vert_dict[frm].add_neighbor(to, cost)


    def delete_edge(self,frm,to):
        self.vert_dict[frm].delete_neighbor(self.vert_dict[to])


    def check_edge_existed(self,frm,to):
        return self.vert_dict[frm].check_neighbor_existed(to)

    def get_vertices(self):
        return self.vert_dict.keys()

    #save the current vert_dict with given fileName
    #input: fileName as a string
    def saveFile(self,fileName):
        newDict=self.vert_dict
        output = open(fileName+'.pkl', 'wb')
        pickle.dump(newDict, output)
        output.close()

    #load the stored vert_dict with having the name fileName
    #input: fileName as a string
    #output: vert_dict
    def loadFile(self,fileName):
        # read python dict back from the file
        file = open(fileName+'.pkl', 'rb')
        dict = pickle.load(file)
        file.close()
        return dict

    #see all the .pkl files name
    #output: all the names as a list
    def fileNames(self):
        temp=[]
        for i in os.listdir(os.getcwd()):
            if '.pkl' in i:
                temp.append(i)
        return temp

#
# g=Graph()
# # g.add_vertex(0)
# # g.add_vertex(1)
# # g.add_edge(0,1,1)
# # g.saveFile('junk')
# # print(g.fileNames())
# dict=g.loadFile('junk')
# for v in dict:#####
#     print(str(dict[v].get_id())+' is connected to '+str([g for g in dict[v]]))