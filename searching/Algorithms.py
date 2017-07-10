import math, numpy,Linking,queue,random

class algorithms:
    def __init__(self,dict):
        self.graph = dict

    ##Call this method when you want BFS or DFS. It can also be iterated if called by 'iterative'.
    # input:@arg1 start node, @arg2 goal node, @arg3 algorithm
    #output: the final path as a list
    def bdfs(self, start, goal,algorithm,it=-1):
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
            if algorithm=='BFS':
                (node,path) = qs.pop(0)#pop(0) means from head
            elif algorithm=='DFS':
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

    ##Call this method when you want UCS or A*. It can also be iterated if called by 'iterative'.
    # input: @arg1 start node, @arg2 goal node, @arg3 algorithm, @arg4 iterate how many layers
    #output: the final path as a list.  ie. [0, 1, 4]  means from 0 to 1 to 4
    def ucsAStar(self, start, goal,algorithm,it=-1):
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
                            if algorithm=='UCS':
                               newCost=cost+self.graph[node].get_weight(adj)#cost +weight of adj
                            elif algorithm=='aStar':#A*
                                heu=self.graph[adj].heuristic
                                newCost=cost+self.graph[node].get_weight(adj)+heu# +heuristic of adj
                            temp.put((newCost,adj,path+[adj]))
                            self.layerDict[adj]=self.layerDict[node]+1#layer of child = layer of parent +1
                    pq.queue.extend(temp.queue)
                pq.queue.sort()#first sort by cost, then sort by numerical order
                self.qsLog.append([node,[n[1] for n in pq.queue]])
                # print('bdfs:'+str(qs))

    ##Call this method when you want an iterative algorithm
    # input:@arg1 start node, @arg2 goal node, @arg3 algorithm, @arg4 iterate deep.
    #output: the final path as a list
    def iterative(self,start, goal,algorithm,it):
        self.qsLog=[]
        self.visitedLog =[]
        # self.layerDict={}
        for i in range(it):
            rtn=None
            self.maxDepth=i+1
            if algorithm in ('BFS','DFS'):
                rtn = self.bdfs(start,goal,algorithm,it)
            elif algorithm in ('UCS','aStar'):
                rtn = self.ucsAStar(start,goal,algorithm,it)
            if rtn:
                return rtn
        return None
    ##after an algorithm executed, it will generate a log of expending node and corresponding queue/stack for each step from the begining to the end.
    #output: queue log/ stack log  ie. [[expending node,[queue/stack]],...]
    def getQsLog(self):
        return self.qsLog
    ##after an algorithm executed, it will generate a log of visited nodes for each step from the begining to the end.
    #output: visited nodes log  ie. [[visited nodes],...]
    def getVisitedLog(self):
        return  self.visitedLog


    ##The miniMax, expectiMiniMax, and alphaBeta algorithm (expectiMiniMax algorithm key word is 'exMiniMax')
    #input:@arg1 the root node, @arg2 how many layers it will goes, @arg3 algorithm
    #output: a list [[expending node, alpha, beta], ...] the root node is always on depth 0
    def miniMaxAlphaBeta(self,id,depth,algorithm):
        self.utilityLog=[]#[[expending node,{id: utility}], ...]
        self.partOfminiMax(id,depth,True,algorithm)
        return self.utilityLog
    #the iterative part of the miniMax algorithm
    def partOfminiMax(self,id,depth,player,algorithm,ab=math.inf):#ab=inf so the root is impossible to be pruned
        if type(self.graph[id]) is Linking.Vertex:#type is vertex
            uti=self.graph[id].utility
            # pro=self.graph[id].probability

        if depth==0 or not self.graph[id].get_connections():#depth==0 or the id is the terminate.
            # temp={}
            # for n in self.graph:
            #     temp[n]=self.graph[n].utility
            self.utilityLog.append([id,uti,uti])#for our term, bestValue is alpha, ab is beta
            return uti
        if player==True:# if player==True
            bestValue= -math.inf
            self.utilityLog.append([id,bestValue,math.inf])#for our term, bestValue is alpha, inf is beta
            for n in self.graph[id].get_connections():#for every child
                if type(self.graph[n]) is Linking.Vertex:#type is vertex
                    if algorithm=='alphaBeta':
                        val=self.partOfminiMax(n,depth-1,False,algorithm,bestValue)
                        if val>ab:#the upper layer will choose the smallest one, so if val>ab means it can be pruned
                            if bestValue<val:#(find the bigger one)
                                # self.graph[id].utility=val
                                bestValue=val
                                self.utilityLog.append([id,val,math.inf])
                            return bestValue#prune
                    else:#miniMax & exMiniMax
                        val=self.partOfminiMax(n,depth-1,False,algorithm)

                    if bestValue<val:
                        # self.graph[id].utility=val
                        bestValue=val
                        if n!=self.graph[id].get_connections()[-1]:
                            self.utilityLog.append([id,val,math.inf])
                else:# type is Action, for exMiniMax
                    bestValue=0
                    for vertid in self.graph[n].neighbor:#go through every child
                        bestValue+=self.graph[vertid].probability*self.partOfminiMax(vertid,depth-1,False,algorithm)
            self.utilityLog.append([id,bestValue,bestValue])#for the last element,  both alpha and beta is bestValue
            return bestValue
        elif player==False:
            bestValue= math.inf
            self.utilityLog.append([id,-math.inf,bestValue])#for opponent's term, -inf is alpha, bestvalue is beta
            for n in self.graph[id].get_connections():#for every child
                if type(self.graph[n]) is Linking.Vertex:#type is vertex
                    if algorithm=='alphaBeta':
                        val=self.partOfminiMax(n,depth-1,True,algorithm,bestValue)
                        if val<ab:#if val < the bestValue of parent means it can be pruned
                            if bestValue>val:
                                # self.graph[id].utility=val
                                bestValue=val
                                self.utilityLog.append([id,-math.inf,val])
                            return bestValue#prune
                    else:#miniMax & exMiniMax
                        val=self.partOfminiMax(n,depth-1,True,algorithm)
                    if bestValue>val:
                        # self.graph[id].utility=val
                        bestValue=val
                        if n!=self.graph[id].get_connections()[-1]:#if it is not the last element
                            self.utilityLog.append([id,-math.inf,val])#alpha is -inf
                else:# type is Action, for exMiniMax
                    bestValue=0
                    for vertid in self.graph[n].neighbor:#go through every child
                        bestValue+=self.graph[vertid].probability*self.partOfminiMax(vertid,depth-1,True,algorithm)
            self.utilityLog.append([id,bestValue,bestValue])#for the last element, both alpha and beta is bestValue
            return bestValue

    ##This will calculate probability values which weren't given in the question, but can be inferred from the information which is given.
    #input: @arg1 list contains the observation variables. ie [id1, id2, ...], @arg2 the id of the node needs to be figured out.
    #output:the probability value of the query node
    def believeNet(self,observation,query):
        self.graph

    def generateProbabilityTable(self):
        self.parent={}#{node id: [parent...], ...}
        self.noParent={i for i in self.graph}#set
        for n in self.graph:#for each node in the graph
            self.graph[n].probabilityTable.clear()#clean up table
            for i in self.graph[n].adjacent:#find each adjacent
                if i in self.noParent:
                    self.noParent.remove(i)
                if i not in self.parent:
                    self.parent[i]=[n]
                else:
                    self.parent[i].append(n)
        for n in self.graph:
            if n in self.parent:#for those who have child
                l=self.parent[n]
                self.graph[n].probabilityTable={n: l}#the attribute row of the table
                for i in range(2**len(l)-1,-1,-1):
                    key=bin(i)[2:].zfill(len(l)).replace('1','T').replace('0','F')
                    self.graph[n].probabilityTable[key]=[0,0,0,0]#ratio, true,based, expected ratio
            else:
                self.graph[n].probabilityTable={n: ' : P'}#the attribute row of the table
                self.graph[n].probabilityTable['T']=[0,0,0,0]

    ##set up the ProbabilityTable manually
    #input: @arg1 the node, @arg2  key of the row as a string ie. 'TT', @arg3 probability
    def setProbabilityTable(self,id,key,value):
        self.graph[id].probabilityTable[key][3]=value

    def simulateData(self,times):
        for t in range(times):
            temp={}
            for n in self.noParent:
                temp[n]='F'
                if random.random()<=self.graph[n].probabilityTable['T'][3]:
                    temp[n]='T'
                    self.graph[n].probabilityTable['T'][1]+=1
                self.graph[n].probabilityTable['T'][2]+=1
                a=self.graph[n].probabilityTable['T'][1]/self.graph[n].probabilityTable['T'][2]
                self.graph[n].probabilityTable['T'][0]=math.floor(a*100)/100
            for n in self.parent:
                st=''
                temp[n]='F'
                for i in self.parent[n]:
                    st+=str(temp[i])
                if random.random()<=self.graph[n].probabilityTable[st][3]:
                    temp[n]='T'
                    self.graph[n].probabilityTable[st][1]+=1
                self.graph[n].probabilityTable[st][2]+=1
                a=self.graph[n].probabilityTable[st][1]/self.graph[n].probabilityTable[st][2]
                self.graph[n].probabilityTable[st][0]=math.floor(a*100)/100