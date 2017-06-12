import math, numpy,Linking

class algorithms:
    def __init__(self,dict):
        self.graph = dict




    def bfs(self, start, goal):
        self.qsLog=[]
        self.visitedLog =[]
        # maintain a queue of paths
        # #push first path into the queue
        queue = [(start,[start])]
        visited=[]
        while queue:
            # gets the first path in the queue
            (node,path) = queue.pop(0)#pop(0) means from head

            if node == goal:
                self.qsLog.append([node,[n[0] for n in queue]])
                visited.append(node)
                self.visitedLog.append([n for n in visited])
                return path
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            elif node not in visited:
                self.qsLog.append([node,[n[0] for n in queue]])
                visited.append(node)
                self.visitedLog.append([n for n in visited])
                for adj in self.graph[node]:
                    queue.append((adj,path+[adj]))
                # print('bfs:'+str(queue))




    def dfs(self, start, goal):
        #ie this.stackLog - so field variable and can be called by others
        self.qsLog=[]
        self.visitedLog =[]

        stack = [(start,[start])]
        visited=[]
        while stack:
            (node, path) = stack.pop()#pop() means from tail

            if node == goal:
                self.qsLog.append([node,[n[0] for n in stack]])
                visited.append(node)
                self.visitedLog.append([n for n in visited])
                return path
            elif node not in visited:
                self.qsLog.append([node,[n[0] for n in stack]])
                visited.append(node)
                self.visitedLog.append([n for n in visited])
                for adj in self.graph[node]:
                    stack.append((adj, path + [adj]))
                # print('dfs: '+str(stack))

    def getQsLog(self):
        return self.qsLog


    def getVisitedLog(self):
        return  self.visitedLog


# LK=Linking.Graph()
# LK.add_vertex(0)
# LK.add_vertex(1)
# LK.add_vertex(2)
# LK.add_vertex(3)
# LK.add_vertex(4)
# LK.add_vertex(5)
# LK.add_vertex(6)
# LK.add_edge(0,1,1)
# LK.add_edge(0,2,1)
# LK.add_edge(1,3,1)
# LK.add_edge(1,4,1)
# LK.add_edge(4,5,1)
# LK.add_edge(2,6,1)
# AL=algorithms(LK.vert_dict)

# for v in LK.vert_dict:
#     print(str(LK.vert_dict[v].get_id())+' is connected to '+str([g for g in LK.vert_dict[v]]))
# print('bfs: '+str(AL.bfs(0,3)))
# print('dfs: '+str(AL.dfs(0,3)))
# AL.bfs(0,3)
# print(AL.getQueueLog())
# AL.dfs(0,3)
# print(AL.getStackLog())