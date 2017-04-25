import  math,numpy
class manageNode:
    n=0
    #priority queue
    queue=[]
    def __init__(self,size):
        self.size=size
        self.dataNode=numpy.full((size,size),math.inf)
    def remove(self,node):
        self.queue.append(node)
        print(self.queue)
    def inc(self):
        if not self.queue:#if queue isEmpty then returns to whatever number the mainframe method is on
            #as has no other deleted numbers to prioritised as labels
            self.n +=1
            #n-1 ensures you start form node 0 not node 1
            return self.n-1
        else:
            #if queue is not empty, take minimum value in the queue firt
            m= min(self.queue)
            self.queue.remove(m)
            return m