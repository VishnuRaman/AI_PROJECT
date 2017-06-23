import unittest,Algorithms,pickle,Linking

class Test_algorithm(unittest.TestCase):
    g=Linking.Graph()
    # 3 layer absolutely complete perfect tree
    for i in range(7):
        g.add_vertex(i)

    g.add_edge(1,4,1)
    g.add_edge(1,3,1)
    g.add_edge(2,6,1)
    g.add_edge(2,5,1)
    g.add_edge(0,2,1)
    g.add_edge(0,1,1)
    AL=Algorithms.algorithms(g.vert_dict)


    def test_bdfs(self):
        #BFS
        self.assertEqual([0,1,4],self.AL.bdfs(0,4,'BFS'))#Test BFS final path
        qsExpect=[[0, [1, 2]], [1, [2, 3, 4]], [2, [3, 4, 5, 6]], [3, [4, 5, 6]], [4, [5, 6]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test BFS qsLog
        visitedLog=[[0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4]]
        self.assertEqual(visitedLog,self.AL.getVisitedLog())#Test BFS visitedLog
        #DFS
        self.assertEqual([0,1,4],self.AL.bdfs(0,4,'DFS'))#Test DFS final path
        qsExpect=[[0, [1, 2]], [2, [1, 5, 6]], [6, [1, 5]], [5, [1]], [1, [3, 4]], [4, [3]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test DFS qsLog
        visitedLog=[[0], [0, 2], [0, 2, 6], [0, 2, 6, 5], [0, 2, 6, 5, 1], [0, 2, 6, 5, 1, 4]]
        self.assertEqual(visitedLog,self.AL.getVisitedLog())#Test DFS visitedLog
    def test_ucsAStar(self):
        #UCS
        self.assertEqual([0,1,4],self.AL.ucsAStar(0,4,'UCS'))#Test UCS final path
        qsExpect=[[0, [1, 2]], [1, [2, 3, 4]], [2, [3, 4, 5, 6]], [3, [4, 5, 6]], [4, [5, 6]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test UCS qsLog
        visitedLog=[[0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4]]
        self.assertEqual(visitedLog,self.AL.getVisitedLog())#Test UCS visitedLog
