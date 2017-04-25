import  math,numpy

#this class stores everything thats shown on the gui
class guiArray:
    def __init__(self,size,canvas):
        self.size=size
        self.arrowArray=numpy.full((size,size),0)
        self.canvas=canvas
        self.nodeList=[[] for y in range(self.size)]
    def get_nodeList(self):
        return self.nodeList
    def addNode(self,set,node):
        self.nodeList[node]=set
        print(self.nodeList)
    def addArrow(self,fromNode,toNode,arrow):

        #so print will say node you are travelling FROM, it travels DOWN the grid to that node
        #then travels ACROSS to find the node you're travelling TO
        self.arrowArray[fromNode][toNode]=arrow
        print(self.arrowArray)
    def deleteNode(self,node):
        for i in range(2):
            self.canvas.delete(self.nodeList[node][i])
        self.nodeList[node]=[]
        print(self.nodeList)

    def deleteArrow(self,node):
        for i in range(self.size):
            if self.arrowArray[node][i]!=0:
               self.canvas.delete(self.arrowArray[node][i])
            if self.arrowArray[i][node]!=0:
               self.canvas.delete(self.arrowArray[i][node])
