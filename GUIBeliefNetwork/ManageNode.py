import  math,numpy
class manageNode:
    n=0
    queue=[]
    def __init__(self,size):
        self.size=size
        self.dataNode=numpy.full((size,size),math.inf)
    def remove(self,node):
        self.queue.append(node)
        print(self.queue)
    def inc(self):
        if not self.queue:#if queue isEmpty
            self.n +=1
            return self.n-1
        else:
            m= min(self.queue)
            self.queue.remove(m)
            return m