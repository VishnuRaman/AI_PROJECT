import math, numpy,Linking,queue

class algorithms:
    def __init__(self,dict):
        self.graph = dict

    #Call this method when you want BFS or DFS. It can also be iterated if called by 'iterative'.
    # input: start node, goal node, algorithm
    #output: the final path as a list
    def bdfs(self, start, goal,switch,it=-1):
        if it == -1:
            self.qsLog=[]
            self.visitedLog =[]
            self.maxDepth=math.inf
        self.layerDict={}
        self.layerDict[start]=0#initialize root as layer 0
        qs = [(start,[start])]#push first path into the queue
        visited=[]
        while qs:
            # gets the first path in the queue
            if switch=='BFS':
                (node,path) = qs.pop(0)#pop(0) means from head
            elif switch=='DFS':
                (node, path) = qs.pop()#pop() means from tail

            if node == goal:
                self.qsLog.append([node,[n[0] for n in qs]])
                visited.append(node)
                self.visitedLog.append([n for n in visited])
                return path
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            elif node not in visited:
                visited.append(node)
                self.visitedLog.append([n for n in visited])
                if (it!=-1 and self.maxDepth>self.layerDict[node]) or (it==-1):#max layer > current layer
                    temp=[]
                    for adj in self.graph[node]:
                        if adj not in [n[0] for n in qs] and adj not in visited:#avoid duplicated node, avoid visited node
                            temp.append((adj,path+[adj]))
                            self.layerDict[adj]=self.layerDict[node]+1#layer of child = layer of parent +1
                    temp.sort()#make sure expand in numerical sequence
                    qs.extend(temp)
                self.qsLog.append([node,[n[0] for n in qs]])

    #Call this method when you want UCS or A*. It can also be iterated if called by 'iterative'.
    # input: start node, goal node, algorithm
    #output: the final path as a list
    def ucsAStar(self, start, goal,switch,it=-1):
        if it == -1:
            self.qsLog=[]
            self.visitedLog =[]
            self.maxDepth=math.inf
        self.layerDict={}
        self.layerDict[start]=0#initialize root as layer 0

        cost=0
        pq = queue.PriorityQueue()
        pq.put((cost,start,[start]))
        visited=[]
        while pq.queue:
            # gets the first path in the queue
            (cost, node, path) = pq.get()
            if node == goal:
                self.qsLog.append([node,[n[1] for n in pq.queue]])
                visited.append(node)
                self.visitedLog.append([n for n in visited])
                return path
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            elif node not in visited:
                visited.append(node)
                self.visitedLog.append([n for n in visited])
                if (it!=-1 and self.maxDepth>self.layerDict[node]) or (it==-1):#max layer > current layer
                    temp=queue.PriorityQueue()
                    for adj in self.graph[node]:
                        if adj not in [n[1] for n in pq.queue] and adj not in visited:#avoid duplicated node, avoid visited node
                            if switch=='UCS':
                               newCost=cost+self.graph[node].get_weight(adj)
                            elif switch=='aStar':#A*
                                newCost=cost+self.graph[node].get_weight(adj)#need +heuristic
                            temp.put((newCost,adj,path+[adj]))
                            self.layerDict[adj]=self.layerDict[node]+1#layer of child = layer of parent +1
                    pq.queue.extend(temp.queue)
                self.qsLog.append([node,[n[1] for n in pq.queue]])
                # print('bdfs:'+str(qs))

    #Call this method when you want an iterative algorithm
    # input: start node, goal node, algorithm, iterate deep
    #output: the final path as a list
    def iterative(self,start, goal,switch, it):
        self.qsLog=[]
        self.visitedLog =[]
        # self.layerDict={}
        for i in range(it):
            rtn=None
            self.maxDepth=i+1
            if switch in ('BFS','DFS'):
                rtn = self.bdfs(start,goal,switch,it)
            elif switch in ('UCS','aStar'):
                rtn = self.ucsAStar(start,goal,switch,it)
            if rtn:
                return rtn
        return None



    def getQsLog(self):
        return self.qsLog

    def getVisitedLog(self):
        return  self.visitedLog