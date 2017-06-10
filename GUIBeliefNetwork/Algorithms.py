import math, numpy,Linking

class algorithms:
    def __init__(self,dict):
        self.graph = dict




    def bfs(self, start, goal):
        self.queueLog=[]
        # maintain a queue of paths
        # #push first path into the queue
        queue = [(start,[start])]


        visited = set()
        while queue:


            # gets the first path in the queue
            (node,path) = queue.pop(0)#pop(0) means from head


            # gets the last node from the path
            # for vertex in path:
            #timo:why the above 'for loop' is needed?
            # path found
            if node == goal:
                self.queueLog.append((node,[n[0] for n in queue]))
                return path
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            elif node not in visited:
                visited.add(node)
                for adj in self.graph[node]:
                    # new_path = list(path)
                    # new_path.append(adj)
                    queue.append((adj,path+[adj]))
                print(queue)
                self.queueLog.append((node,[n[0] for n in queue]))




    def dfs(self, start, goal):
        self.stackLog=[]
        visited = set()
        stack = [(start,[start])]

        while stack:
            (node, path) = stack.pop()#pop() means from tail

            # for node in path:
            #timo:why the above 'for loop' is needed?
            if node == goal:
                self.stackLog.append((node,[n[0] for n in stack]))
                return path
            elif node not in visited:
                visited.add(node)
                for adj in self.graph[node]:
                    stack.append((adj, path + [adj]))
                self.stackLog.append((node,[n[0] for n in stack]))
                print(stack)

    def getQueueLog(self):
        return self.queueLog

    def getStackLog(self):
        return self.stackLog

LK=Linking.Graph()
LK.add_vertex(0)
LK.add_vertex(1)
LK.add_vertex(2)
LK.add_vertex(3)
LK.add_vertex(4)
LK.add_vertex(5)
LK.add_vertex(6)
LK.add_edge(0,1,1)
LK.add_edge(0,2,1)
LK.add_edge(1,3,1)
LK.add_edge(1,4,1)
LK.add_edge(4,5,1)
LK.add_edge(2,6,1)
AL=algorithms(LK.vert_dict)

# for v in LK.vert_dict:
#     print(str(LK.vert_dict[v].get_id())+' is connected to '+str([g for g in LK.vert_dict[v]]))
# print('bfs: '+str(AL.bfs(0,3)))
# print('dfs: '+str(AL.dfs(0,3)))
AL.bfs(0,3)
print(AL.getQueueLog())
# AL.dfs(0,3)
# print(AL.getStackLog())