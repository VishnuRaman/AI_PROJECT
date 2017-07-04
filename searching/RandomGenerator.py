import Linking,random
class randomGenerator:
    def randomGraph(self,branch,layer,lowerBound,upperBound):
        LK=Linking.Graph()
        LK.add_vertex(0)#root
        queue=[LK.get_vertex(0).id]
        nodeId=1
        layerDict={0:0}

        while queue:#queue is not empty
            parent=queue.pop(0)#pop from head
            if layer>layerDict[parent]:
                for i in range(branch):
                    LK.add_vertex(nodeId)
                    LK.add_edge(parent,nodeId)
                    layerDict[nodeId]=layerDict[parent]+1
                    queue.append(nodeId)
                    nodeId+=1
        for n in LK.get_vertices():
            if not LK.get_vertex(n).get_connections():
                LK.get_vertex(n).utility=random.randint(lowerBound,upperBound)
        return LK
