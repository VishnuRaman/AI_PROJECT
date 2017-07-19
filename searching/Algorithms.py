import math, numpy,Linking,queue,random,re

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
                self.visitedLog.append(list(visited))
                return path
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            elif node not in visited:
                visited.append(node)
                self.visitedLog.append(list(visited))
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
    def refreshP(self,observation):
        PT={}
        for i in self.graph:
            PT[i]=self.query(observation,i)
        return PT
    ##This will calculate probability values which weren't given in the question, but can be inferred from the information which is given.
    #input: @arg1 dictionary contains the observation variables and its boolean. ie {id:'T', ...}, @arg2 the id of the node needs to be figured out.
    #output:the probability value of the query node
    def query(self,observation,query):
        self.observation=observation
        self.tempPT={}
        for i in self.graph:
            self.tempPT[i]=self.graph[i].probability
        for i in observation:
            if observation[i]=='T':
                self.tempPT[i]=1
            else:
                self.tempPT[i]=0
        if query in observation:
            return self.tempPT[query]
        return self.believeNet(query,[])
    ##the recursive part of query
    def believeNet(self,query,visited):
        visited.append(query)
        if not self.observation:#empty
            return self.tempPT[query]
        if query in self.parent:#have parent
            for p in self.parent[query]:#for every parent not in visited
                if p not in visited:
                    if p in self.observation:
                        self.tempPT[query]=self.updateSelfProbabilityFromParent(query)
                    else:
                        ori=self.tempPT[p]
                        new=self.believeNet(p,visited)
                        if ori!=new:#it changed
                            self.tempPT[query]=self.updateSelfProbabilityFromParent(query)
        for a in self.graph[query].get_connections():
            if a not in visited:
                if a in self.observation:
                    self.tempPT[query]=self.updateParentObs(a,query)
                else:
                    self.findParentAndChild(query)
                    boolean=False
                    for o in self.observation:
                        if o in self.relatedChild:
                            boolean=True
                    if boolean:
                        ori=self.tempPT[a]
                        new=self.believeNet(a,visited)
                        if ori!=new:#non observation and changed
                            self.tempPT[query]=self.updateParentObs(a,query)*new+self.updateParentObs(a,query,True)*(1-new)
        return self.tempPT[query]
    def findParentAndChild(self,query):
        self.relatedParent=[]#a list of nodes that will affect the value of query node
        if query in self.parent:
            q=list(self.parent[query])
            self.relatedParent.extend(q)
            while q:
                p=q.pop(0)
                if p in self.parent:
                    l=list(self.parent[p])
                    q.extend(l)
                    self.relatedParent.extend(l)
        self.relatedChild=[]
        q=list(self.graph[query].adjacent)
        self.relatedChild.extend(q)
        while q:
            a=q.pop(0)
            c=list(self.graph[a].adjacent)
            q.extend(c)
            self.relatedChild.extend(c)
    def updateParentObs(self,id,parentId,non=False):
        parent=self.parent[id]
        st=''
        for i in range(len(parent)):
            if parent[i]==parentId:
                if non==False:
                    st+='T'
                else:
                    st+='F'
            else:
                st=st+'.'
        nu=0
        de=0
        for k in self.graph[id].probabilityTable:
            if k != id:#skip title row
                pro=1
                for m in range(len(k)):
                    if k[m]=='T':
                        pro*=self.tempPT[self.parent[id][m]]
                    elif k[m]=='F':
                        pro*=(1-self.tempPT[self.parent[id][m]])
                if id in self.observation:
                    if self.observation[id]=='T':
                        pro*=self.graph[id].probabilityTable[k][0]#happening ratio*simulated ratio
                    else:
                        pro*=(1-self.graph[id].probabilityTable[k][0])
                else:
                    pro*=self.graph[id].probabilityTable[k][0]#happening ratio*simulated ratio
                if re.match(st,k)!=None:
                    nu+=pro
                else:
                    de+=pro
        return nu/(nu+de)
    def updateSelfProbabilityFromParent(self,id):
        st=''
        for p in self.parent[id]:
            if p in self.observation:
                st+=self.observation[p]
            else:
                st+='.'
        nu=0
        de=0
        for k in self.graph[id].probabilityTable:
            if k != id:#skip title row
                pro=1
                pro2=1
                for m in range(len(k)):
                    if k[m]=='T':
                        pro*=self.tempPT[self.parent[id][m]]
                    elif k[m]=='F':
                        pro*=(1-self.tempPT[self.parent[id][m]])
                pro2*=pro*(1-self.graph[id].probabilityTable[k][0])
                pro*=self.graph[id].probabilityTable[k][0]#happening ratio*simulated ratio

                if re.match(st,k)!=None:
                    nu+=pro
                    de+=pro2
        return nu/(nu+de)

    def generateProbabilityTable(self):
        self.parent={}#{node id: [parent...], ...} the nodes which have parent
        for n in self.graph:#for each node in the graph
            self.graph[n].probabilityTable.clear()#clean up table
            for i in self.graph[n].adjacent:#find each adjacent
                if i not in self.parent:
                    self.parent[i]=[n]
                else:
                    self.parent[i].append(n)
        self.noParent={i for i in self.graph if i not in self.parent}#set, the nodes have no parent
        for n in self.graph:
            if n in self.parent:#for those who have parent
                l=self.parent[n]
                self.graph[n].probabilityTable={n: l}#the attribute row of the table
                for i in range(2**len(l)-1,-1,-1):
                    key=bin(i)[2:].zfill(len(l)).replace('1','T').replace('0','F')
                    self.graph[n].probabilityTable[key]=[0,0,0,0]#ratio, true,based, expected ratio
            else:#prior
                self.graph[n].probabilityTable={n:[]}#the attribute row of the table
                self.graph[n].probabilityTable['T']=[0,0,0,0]

    ##set up the ProbabilityTable manually
    #input: @arg1 the node, @arg2  key of the row as a string ie. 'TT', @arg3 probability
    def setProbabilityTable(self,id,key,value):
        self.graph[id].probabilityTable[key][3]=value

    def simulateData(self,times):
        for t in range(times):
            temp={}
            for n in self.noParent:#prior
                temp[n]='F'
                rowT=self.graph[n].probabilityTable['T']
                if random.random()<=rowT[3]:
                    temp[n]='T'
                    rowT[1]+=1
                rowT[2]+=1
                a=rowT[1]/rowT[2]
                rowT[0]=math.floor(a*100)/100
            queue=list(self.parent)#clone it and become a queue
            while queue:#is not empty
                q=queue.pop(0)#pop from head
                if set(self.parent[q]).issubset(temp):#if all parents are ready
                    st=''
                    temp[q]='F'
                    table=self.graph[q].probabilityTable
                    for i in self.parent[q]:
                        st+=str(temp[i])
                    if random.random()<=table[st][3]:
                        temp[q]='T'
                        table[st][1]+=1
                    table[st][2]+=1
                    a=table[st][1]/table[st][2]
                    table[st][0]=math.floor(a*1000)/1000
                else:
                    queue.append(q)#add to tail
        #after all simulating, update the prior probability of each node  (without given condition)
        self.order=[]#the order that all parents of node are ready
        for n in self.noParent:
            self.graph[n].probability=self.graph[n].probabilityTable['T'][0]
            self.order.append(n)
        queue=list(self.parent)#clone it and become a queue
        while queue:#is not empty
            q=queue.pop(0)#pop from head
            if set(self.parent[q]).issubset(self.order):#if all parents are ready
                self.order.append(q)
                k=0
                for j in self.graph[q].probabilityTable:
                    if j != q:
                        k+=self.graph[q].probabilityTable[j][1]
                        self.graph[q].probability=k/(times)
            else:
                queue.append(q)
    ##manually set up the ratio in probability table, after set up, setKnownPT should be called
    #input:@arg1 the node, @arg2  key of the row as a string ie. 'TT', @arg3 probability
    def setKnownPT(self,id,key,value):
        self.graph[id].probabilityTable[key][0]=value

    ##update the probability of each node  (without given condition)
    def generatePriorProbability(self):
        self.order=[]#the order that all parents of node are ready
        for n in self.noParent:
            self.graph[n].probability=self.graph[n].probabilityTable['T'][0]
            self.order.append(n)
        queue=list(self.parent)#clone it and become a queue
        while queue:#is not empty
            q=queue.pop(0)#pop from head
            if set(self.parent[q]).issubset(self.order):#if all parents are ready
                self.order.append(q)
                nu=0
                de=0
                for k in self.graph[q].probabilityTable:
                    if k != q:#skip title row
                        pro=1
                        pro2=1
                        for m in range(len(k)):
                            if k[m]=='T':
                                pro*=self.graph[self.parent[q][m]].probability
                            elif k[m]=='F':
                                pro*=(1-self.graph[self.parent[q][m]].probability)
                        pro2*=pro*(1-self.graph[q].probabilityTable[k][0])
                        pro*=self.graph[q].probabilityTable[k][0]#happening ratio*simulated ratio
                        nu+=pro
                        de+=pro2
                self.graph[q].probability=nu/(nu+de)
            else:
                queue.append(q)