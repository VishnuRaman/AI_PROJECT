import  math,numpy
class beliefManageNode:
    n=0
    #priority queue
    queue=[]

    def remove(self,node):
        self.queue.append(node)
    def inc(self):
        if not self.queue:

            # for empty queues, return the current number being evaluated
            # as there are no currently deleted numbers to be prioritised for assignment
            self.n +=1

            #n-1 ensures you start form node 0 not node 1
            return self.n-1
        else:
            #itake minimum value first from the non empty queue
            m= min(self.queue)
            self.queue.remove(m)
            return m
