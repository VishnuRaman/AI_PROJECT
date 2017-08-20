import  Algorithms,Linking,math,RandomGenerator
class al_data:
    g=Linking.Graph()
    for i in range(9):
        g.add_vertex(i)
    g.add_edge(0,1)
    g.add_edge(1,0)
    g.add_edge(0,2)
    g.add_edge(2,0)
    g.add_edge(0,6)
    g.add_edge(6,0)
    g.add_edge(1,3)
    g.add_edge(3,1)
    g.add_edge(1,4)
    g.add_edge(4,1)
    g.add_edge(2,5)
    g.add_edge(5,2)
    g.add_edge(2,6)
    g.add_edge(6,2)
    g.add_edge(6,4)
    g.add_edge(4,6)
    g.add_edge(6,7)
    g.add_edge(7,6)
    g.add_edge(7,8)
    g.add_edge(8,7)
    g.add_edge(8,3)
    g.add_edge(3,8)

    h=Linking.Graph()
    for i in range(9):
        h.add_vertex(i)
    h.add_edge(0,1)
    h.add_edge(1,0)
    h.add_edge(0,2,2)
    h.add_edge(2,0,2)
    h.add_edge(0,6,2.2)
    h.add_edge(6,0,2.2)
    h.add_edge(1,3,2.2)
    h.add_edge(3,1,2.2)
    h.add_edge(1,4,1.4)
    h.add_edge(4,1,1.4)
    h.add_edge(2,5)
    h.add_edge(5,2)
    h.add_edge(2,6)
    h.add_edge(6,2)
    h.add_edge(6,4,1.4)
    h.add_edge(4,6,1.4)
    h.add_edge(6,7)
    h.add_edge(7,6)
    h.add_edge(7,8,2)
    h.add_edge(8,7,2)
    h.add_edge(8,3,2)
    h.add_edge(3,8,2)


    def run(self,goal):
        l=[['BFS',0], ['DFS',0], ['UCS',0], ['aStar',0], ['BFS',1], ['DFS',1], ['UCS',1], ['aStar',1]]
        for i in l:
            if i[1]==0:
                print('**'+str(i[0]))
            else:
                print('**iter '+str(i[0]))

            if i[0] in ('BFS','DFS'):
                if i[1]==0:
                    self.al.bdfs(0,goal,i[0])
                else:
                    self.al.iterative(0,goal,i[0],2)
            else:
                if i[1]==0:
                    self.al.ucsAStar(0,goal,i[0])
                else:
                    self.al.iterative(0,goal,i[0],2)
            count=0
            # print(self.al.getQsLog())
            for item in self.al.getQsLog():
                count+=len(item[1])
            avg=count/len(self.al.getQsLog())
            print('Steps: '+str(len(self.al.getQsLog())))
            print('Avg:                       '+str(avg))

    def CGH(self):
        print('CGH')
        #Costs are the same
        #Goal is found
        #With Heuristic
        G=self.g
        G.get_vertex(0).heuristic=3
        G.get_vertex(1).heuristic=2
        G.get_vertex(2).heuristic=3
        G.get_vertex(3).heuristic=1
        G.get_vertex(4).heuristic=0
        G.get_vertex(5).heuristic=4
        G.get_vertex(6).heuristic=2
        G.get_vertex(7).heuristic=3
        G.get_vertex(8).heuristic=3
        self.al=Algorithms.algorithms(G.vert_dict)
        self.run(4)

    def CGh(self):
        print('CGh')
        #Costs are the same
        #Goal is found
        #Without Heuristic
        G=self.g
        self.al=Algorithms.algorithms(G.vert_dict)
        self.run(4)

    def CgH(self):
        print('CgH')
        #Costs are the same
        #Goal is not found
        #With Heuristic
        G=self.g
        G.get_vertex(0).heuristic=3
        G.get_vertex(1).heuristic=2
        G.get_vertex(2).heuristic=3
        G.get_vertex(3).heuristic=1
        G.get_vertex(4).heuristic=0
        G.get_vertex(5).heuristic=4
        G.get_vertex(6).heuristic=2
        G.get_vertex(7).heuristic=3
        G.get_vertex(8).heuristic=3
        self.al=Algorithms.algorithms(G.vert_dict)
        self.run(9)

    def Cgh(self):
        print('Cgh')
        #Costs are the same
        #Goal is not found
        #Without Heuristic
        G=self.g
        self.al=Algorithms.algorithms(G.vert_dict)
        self.run(9)

    def cGH(self):
        print('cGH')
        #Costs are the same
        #Goal is found
        #With Heuristic
        G=self.h
        G.get_vertex(0).heuristic=3
        G.get_vertex(1).heuristic=2
        G.get_vertex(2).heuristic=3
        G.get_vertex(3).heuristic=1
        G.get_vertex(4).heuristic=0
        G.get_vertex(5).heuristic=4
        G.get_vertex(6).heuristic=2
        G.get_vertex(7).heuristic=3
        G.get_vertex(8).heuristic=3
        self.al=Algorithms.algorithms(G.vert_dict)
        self.run(4)

    def cGh(self):
        print('cGh')
        #Costs are the same
        #Goal is found
        #Without Heuristic
        G=self.h
        self.al=Algorithms.algorithms(G.vert_dict)
        self.run(4)

    def cgH(self):
        print('cgH')
        #Costs are the same
        #Goal is not found
        #With Heuristic
        G=self.h
        G.get_vertex(0).heuristic=3
        G.get_vertex(1).heuristic=2
        G.get_vertex(2).heuristic=3
        G.get_vertex(3).heuristic=1
        G.get_vertex(4).heuristic=0
        G.get_vertex(5).heuristic=4
        G.get_vertex(6).heuristic=2
        G.get_vertex(7).heuristic=3
        G.get_vertex(8).heuristic=3
        self.al=Algorithms.algorithms(G.vert_dict)
        self.run(9)

    def cgh(self):
        print('cgh')
        #Costs are the same
        #Goal is not found
        #Without Heuristic
        G=self.h
        self.al=Algorithms.algorithms(G.vert_dict)
        self.run(9)
r=al_data()
r.CGH()
# r.CGh()
# r.CgH()
# r.Cgh()
# r.cGH()
# r.cGh()
# r.cgH()
# r.cgh()