import  math,numpy
#this class stores everything thats shown on the gui
class guiArray:
    def __init__(self,canvas):
        self.canvas=canvas
        self.nodeList={}
        self.coordList={}
        # self.xcoord={}
        # self.ycoord={}

    def addNode(self,set,nodeID):
        self.nodeList[nodeID]=set
        print('GUI object '+str(self.nodeList))

    def addCoords(self,set,nodeID):
        self.coordList[nodeID]=set
        print('Coordinates '+str(self.coordList))

    # def addXcoords(self,set,nodeID):
    #     self.coordList[nodeID]=set
    #     print('x = '+str(self.xcoord))

    def addArrow(self,fromNode,toNode,arrow,weight): #include weight after arrow when sorted it out via gui
        #so print will say node you are travelling FROM, it travels DOWN the grid to that node
        #then travels ACROSS to find the node you're travelling TO
        self.nodeList[fromNode][2][toNode]=(arrow, weight) #include ,weight after arrow when sorted it on the gui
        print('GUI object '+str(self.nodeList))#########

    def addBeliefArrow(self, fromNode, toNode, arrow):
        self.nodeList[fromNode][2][toNode] = arrow
        print('GUI object' + str(self.nodeList))

    def deleteNode(self,node):
        self.deleteArrow(node)
        for i in range(2):
            self.canvas.delete(self.nodeList[node][i])
        self.nodeList.pop(node)
        print('GUI object '+str(self.nodeList))#########

    def deleteArrow(self,node):
        for i in self.nodeList[node][2]:#delete the links from the node to anywhere
            self.canvas.delete(self.nodeList[node][2][i][0])#delete arrow
            self.canvas.delete(self.nodeList[node][2][i][1])#delete text
        for n in self.nodeList:#delete the links from anywhere to the node
            if node in self.nodeList[n][2]:
                self.canvas.delete(self.nodeList[n][2][node][0])#delete arrow
                self.canvas.delete(self.nodeList[n][2][node][1])#delete text
                self.nodeList[n][2].pop(node)


#add in the methods for the boxes with the minmax gui
