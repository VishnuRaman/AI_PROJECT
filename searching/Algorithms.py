import math, numpy,Linking,queue

class algorithms:
    def __init__(self,dict):
        self.graph = dict

    def bdfs(self, start, goal,switch):
        self.qsLog=[]
        self.visitedLog =[]
        # maintain a queue of paths
        # #push first path into the queue
        qs = [(start,[start])]

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
                temp=[]
                for adj in self.graph[node]:
                    if adj not in [n[0] for n in qs] and adj not in visited:#avoid duplicated node, avoid visited node
                        temp.append((adj,path+[adj]))
                temp.sort()#make sure expand in numerical sequence
                qs.extend(temp)
                self.qsLog.append([node,[n[0] for n in qs]])
                # print('bdfs:'+str(qs))

    def ucsAStar(self, start, goal):
        self.qsLog=[]
        self.visitedLog =[]
        # maintain a queue of paths
        # #push first path into the queue
        cost=0
        pq = queue.PriorityQueue()
        pq.put((cost,start,[start]))


        visited=[]
        while pq:
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
                temp=queue.PriorityQueue()
                for adj in self.graph[node]:
                    if adj not in [n[1] for n in pq.queue] and adj not in visited:#avoid duplicated node, avoid visited node
                        newCost=cost+self.graph[node].get_weight(adj)
                        temp.put((newCost,adj,path+[adj]))
                pq.queue.extend(temp.queue)
                self.qsLog.append([node,[n[1] for n in pq.queue]])
                # print('bdfs:'+str(qs))


    def getQsLog(self):
        return self.qsLog

    def getVisitedLog(self):
        return  self.visitedLog