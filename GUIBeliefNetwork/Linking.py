import  math,numpy
class Linking(object):
    def __init__(self,size):
        self.size=size
        self.dataLinking=numpy.full((size,size),math.inf)
    def connect(self,thisNodeId,tarNodeId,weight):
        self.dataLinking[thisNodeId][tarNodeId]=weight
    def disconnect(self,thisNodeId,tarNodeId):
        self.dataLinking[thisNodeId][tarNodeId]=math.inf
    def deleteNode(self,node):
        for i in range(self.size):
            self.dataLinking[node][i]=math.inf
            self.dataLinking[i][node]=math.inf