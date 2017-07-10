import Linking,random,Algorithms
class randomGenerator:
    ##This is a method can automatically generate a graph and given those leaves a random utility
    #input:@arg1 branch of the each subtree, @arg2 layers of the whole tree, @arg3 lower boundary of the utility, @arg4 upper boundary of the utility
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


# g=randomGenerator().randomGraph(2,2,-2,2)
# g.delete_edge(2,5)
# g.delete_edge(2,6)
# g.add_objEdge('a0')
# g.add_edge(2,'a0')
# g.add_objEdge_vert_connection('a0',5)
# g.add_objEdge_vert_connection('a0',6)
# g.get_vertex(5).probability=0.2
# g.get_vertex(6).probability=0.8
# a=Algorithms.algorithms(g.vert_dict).miniMaxAlphaBeta(0,2,'exMiniMax')
# for n in g:
#     if type(n) is Linking.Vertex:
#         if not n.get_connections():
#             print(str(n.id)+'\'s utility is '+str(n.utility))
# print()
# for e in a:
#     print(e)