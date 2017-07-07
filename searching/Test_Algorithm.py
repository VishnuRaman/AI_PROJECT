import unittest,Algorithms,Linking,math,RandomGenerator

class Test_algorithm(unittest.TestCase):
    g=Linking.Graph()
    gd=Linking.Grid(3,3)#3*3 grid

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
    AL_gd=Algorithms.algorithms(gd.grid_dict)

#For Graph data structure
    def test_bdfs_bfs(self):
        #BFS
        self.assertEqual([0,1,4],self.AL.bdfs(0,4,'BFS'))#Test BFS final path
        qsExpect=[[0, [1, 2]], [1, [2, 3, 4]], [2, [3, 4, 5, 6]], [3, [4, 5, 6]], [4, [5, 6]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test BFS qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test BFS visitedLog
    def test_bdfs_dfs(self):
        #DFS
        self.assertEqual([0,1,4],self.AL.bdfs(0,4,'DFS'))#Test DFS final path
        qsExpect=[[0, [1, 2]], [2, [1, 5, 6]], [6, [1, 5]], [5, [1]], [1, [3, 4]], [4, [3]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test DFS qsLog
        visitedExpect=[[0], [0, 2], [0, 2, 6], [0, 2, 6, 5], [0, 2, 6, 5, 1], [0, 2, 6, 5, 1, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test DFS visitedLog
    def test_ucsAStar_ucs(self):
        #UCS
        self.assertEqual([0,1,4],self.AL.ucsAStar(0,4,'UCS'))#Test UCS final path
        qsExpect=[[0, [1, 2]], [1, [2, 3, 4]], [2, [3, 4, 5, 6]], [3, [4, 5, 6]], [4, [5, 6]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test UCS qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test UCS visitedLog
    def test_ucsAStar_aStar(self):
        #A* (manual heuristic)
        self.g.get_vertex(1).heuristic=1
        self.g.get_vertex(3).heuristic=1
        self.assertEqual([0,1,4],self.AL.ucsAStar(0,4,'aStar'))#Test A* final path
        qsExpect=[[0, [2, 1]], [2, [1, 5, 6]], [1, [5, 6, 4, 3]], [5, [6, 4, 3]], [6, [4, 3]], [4, [3]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test A* qsLog
        visitedExpect=[[0], [0, 2], [0, 2, 1], [0, 2, 1, 5], [0, 2, 1, 5, 6], [0, 2, 1, 5, 6, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test A* visitedLog
        self.g.resetAllHeuristic()
        #A* (default heuristic=0)
        self.assertEqual([0,1,4],self.AL.ucsAStar(0,4,'aStar'))#Test A* final path
        qsExpect=[[0, [1, 2]], [1, [2, 3, 4]], [2, [3, 4, 5, 6]], [3, [4, 5, 6]], [4, [5, 6]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test A* qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test A* visitedLog
    def test_bdfs_bfs_iter(self):
        #BFS
        self.assertEqual([0,1,4],self.AL.iterative(0,4,'BFS',it=3))#Test BFS final path
        qsExpect=[[0, [1, 2]], [1, [2]], [2, []], [0, [1, 2]], [1, [2, 3, 4]], [2, [3, 4, 5, 6]], [3, [4, 5, 6]], [4, [5, 6]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test BFS qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 2], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test BFS visitedLog
    def test_bdfs_dfs_iter(self):
        #DFS
        self.assertEqual([0,2,5],self.AL.iterative(0,5,'DFS',it=3))#Test DFS final path
        qsExpect=[[0, [1, 2]], [2, [1]], [1, []],[0, [1, 2]], [2, [1, 5, 6]], [6, [1, 5]], [5, [1]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test DFS qsLog
        visitedExpect=[[0], [0, 2], [0, 2, 1], [0], [0, 2], [0, 2, 6], [0, 2, 6, 5]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test DFS visitedLog
    def test_ucsAStar_ucs_iter(self):
        #UCS
        self.assertEqual([0,1,4],self.AL.iterative(0,4,'UCS',it=3))#Test UCS final path
        qsExpect=[[0, [1, 2]], [1, [2]], [2, []], [0, [1, 2]], [1, [2, 3, 4]], [2, [3, 4, 5, 6]], [3, [4, 5, 6]], [4, [5, 6]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test UCS qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 2], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test UCS visitedLog
    def test_ucsAStar_aStar_iter(self):
        #A* (manual heuristic)
        self.g.get_vertex(1).heuristic=1
        self.g.get_vertex(3).heuristic=1
        self.assertEqual([0,1,4],self.AL.iterative(0,4,'aStar',it=3))#Test A* final path
        qsExpect=[[0, [2, 1]], [2, [1]], [1, []], [0, [2, 1]], [2, [1, 5, 6]], [1, [5, 6, 4, 3]],[5, [6, 4, 3]], [6, [4, 3]], [4, [3]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test A* qsLog
        visitedExpect=[[0], [0, 2], [0, 2, 1], [0], [0, 2], [0, 2, 1], [0, 2, 1, 5], [0, 2, 1, 5, 6], [0, 2, 1, 5, 6, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test A* visitedLog
        self.g.resetAllHeuristic()
        #A* (default heuristic=0)
        self.assertEqual([0,1,4],self.AL.iterative(0,4,'aStar',it=3))#Test A* final path
        qsExpect=[[0, [1, 2]], [1, [2]], [2, []], [0, [1, 2]], [1, [2, 3, 4]], [2, [3, 4, 5, 6]], [3, [4, 5, 6]], [4, [5, 6]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test A* qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 2], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test A* visitedLog

#For Grid data structure
    def test_bdfs_bfs_grid(self):
        #BFS
        self.assertEqual([0,1,4],self.AL_gd.bdfs(0,4,'BFS'))#Test BFS final path
        qsExpect=[[0, [1, 3]], [1, [3, 2, 4]], [3, [2, 4, 6]], [2, [4, 6, 5]], [4, [6, 5]]]
        self.assertEqual(qsExpect,self.AL_gd.getQsLog())#Test BFS qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 3], [0, 1, 3, 2], [0, 1, 3, 2, 4]]
        self.assertEqual(visitedExpect,self.AL_gd.getVisitedLog())#Test BFS visitedLog
    def test_bdfs_dfs_grid(self):
        #DFS
        self.assertEqual([0,3,4],self.AL_gd.bdfs(0,4,'DFS'))#Test DFS final path
        qsExpect=[[0, [1, 3]], [3, [1, 4, 6]], [6, [1, 4, 7]], [7, [1, 4, 8]], [8, [1, 4, 5]], [5, [1, 4, 2]], [2, [1, 4]], [4, [1]]]
        self.assertEqual(qsExpect,self.AL_gd.getQsLog())#Test DFS qsLog
        visitedExpect=[[0], [0, 3], [0, 3, 6], [0, 3, 6, 7], [0, 3, 6, 7, 8], [0, 3, 6, 7, 8, 5], [0, 3, 6, 7, 8, 5, 2], [0, 3, 6, 7, 8, 5, 2, 4]]
        self.assertEqual(visitedExpect,self.AL_gd.getVisitedLog())#Test DFS visitedLog
    def test_ucsAStar_ucs_grid(self):
        #UCS
        self.assertEqual([0,1,4],self.AL_gd.ucsAStar(0,4,'UCS'))#Test UCS final path
        qsExpect=[[0, [1, 3]], [1, [3, 2, 4]], [3, [2, 4, 6]], [2, [4, 6, 5]], [4, [6, 5]]]
        self.assertEqual(qsExpect,self.AL_gd.getQsLog())#Test UCS qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 3], [0, 1, 3, 2], [0, 1, 3, 2, 4]]
        self.assertEqual(visitedExpect,self.AL_gd.getVisitedLog())#Test UCS visitedLog
    def test_ucsAStar_aStar_grid(self):
        #A* (getManhattanDist)
        self.gd.setManhattanDist(4)
        self.assertEqual([0,1,4],self.AL_gd.ucsAStar(0,4,'aStar'))#Test A* final path
        qsExpect=[[0, [1, 3]], [1, [3, 4, 2]], [3, [4, 2, 6]], [4, [2, 6]]]
        self.assertEqual(qsExpect,self.AL_gd.getQsLog())#Test A* qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 3], [0, 1, 3, 4]]
        self.assertEqual(visitedExpect,self.AL_gd.getVisitedLog())#Test A* visitedLog
    def test_bdfs_bfs_iter_grid(self):
        #BFS
        self.assertEqual([0,3,6],self.AL_gd.iterative(0,6,'BFS',it=3))#Test BFS final path
        qsExpect=[[0, [1, 3]], [1, [3]], [3, []], [0, [1, 3]], [1, [3, 2, 4]], [3, [2, 4, 6]], [2, [4, 6]], [4, [6]], [6, []]]
        self.assertEqual(qsExpect,self.AL_gd.getQsLog())#Test BFS qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 3], [0], [0, 1], [0, 1, 3], [0, 1, 3, 2], [0, 1, 3, 2, 4], [0, 1, 3, 2, 4, 6]]
        self.assertEqual(visitedExpect,self.AL_gd.getVisitedLog())#Test BFS visitedLog
    def test_bdfs_dfs_iter_grid(self):
        #DFS
        self.assertEqual([0,3,6],self.AL_gd.iterative(0,6,'DFS',it=3))#Test DFS final path
        qsExpect=[[0, [1, 3]], [3, [1]], [1, []],[0, [1, 3]], [3, [1, 4, 6]], [6, [1, 4]]]
        self.assertEqual(qsExpect,self.AL_gd.getQsLog())#Test DFS qsLog
        visitedExpect=[[0], [0, 3], [0, 3, 1], [0], [0, 3], [0, 3, 6]]
        self.assertEqual(visitedExpect,self.AL_gd.getVisitedLog())#Test DFS visitedLog
    def test_ucsAStar_ucs_iter_grid(self):
        #UCS
        self.assertEqual([0,3,6],self.AL_gd.iterative(0,6,'UCS',it=3))#Test UCS final path
        qsExpect=[[0, [1, 3]], [1, [3]], [3, []], [0, [1, 3]], [1, [3, 2, 4]], [3, [2, 4, 6]], [2, [4, 6]], [4, [6]], [6, []]]
        self.assertEqual(qsExpect,self.AL_gd.getQsLog())#Test UCS qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 3], [0], [0, 1], [0, 1, 3], [0, 1, 3, 2], [0, 1, 3, 2, 4], [0, 1, 3, 2, 4, 6]]
        self.assertEqual(visitedExpect,self.AL_gd.getVisitedLog())#Test UCS visitedLog
    def test_ucsAStar_aStar_iter_grid(self):
        #A* (getManhattanDist)
        self.gd.setManhattanDist(4)
        self.assertEqual([0,1,4],self.AL_gd.iterative(0,4,'aStar',it=3))#Test A* final path
        qsExpect=[[0, [1, 3]], [1, [3]], [3, []], [0, [1, 3]], [1, [3, 4, 2]], [3, [4, 2, 6]], [4, [2, 6]]]
        self.assertEqual(qsExpect,self.AL_gd.getQsLog())#Test A* qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 3], [0], [0, 1], [0, 1, 3], [0, 1, 3, 4]]
        self.assertEqual(visitedExpect,self.AL_gd.getVisitedLog())#Test A* visitedLog
    def test_miniMaxAlphaBeta_miniMax(self):
        self.g.resetAllUtility()
        self.g.get_vertex(3).utility=20
        self.g.get_vertex(4).utility=10
        self.g.get_vertex(5).utility=5
        self.g.get_vertex(6).utility=15
        expect=[[0, -math.inf, math.inf],
                 [1, -math.inf, math.inf],
                 [3, 20, 20],
                 [1, -math.inf, 20],
                 [4, 10, 10],
                 [1, 10, 10],
                 [0, 10, math.inf],
                 [2, -math.inf, math.inf],
                 [5, 5, 5],
                 [2, -math.inf, 5],
                 [6, 15, 15],
                 [2, 5, 5],
                 [0, 10, 10]]
        self.assertListEqual(self.AL.miniMaxAlphaBeta(0,3,'miniMax'),expect)

    def test_miniMaxAlphaBeta_alphaBeta(self):
        self.g.resetAllUtility()
        self.g.get_vertex(3).utility=20
        self.g.get_vertex(4).utility=1
        self.g.get_vertex(5).utility=5
        self.g.get_vertex(6).utility=30
        #without prune
        expect=[[0, -math.inf, math.inf],
                [1, -math.inf, math.inf],
                [3, 20, 20],
                [1, -math.inf, 20],
                [4, 1, 1],
                [1, 1, 1],
                [0, 1, math.inf],
                [2, -math.inf, math.inf],
                [5, 5, 5],
                [2, -math.inf, 5],
                [6, 30, 30],
                [2, 5, 5],
                [0, 5, 5]]

        self.assertListEqual(self.AL.miniMaxAlphaBeta(0,3,'alphaBeta'),expect)
        # #with prune
        self.g.resetAllUtility()
        self.g.get_vertex(3).utility=20
        self.g.get_vertex(4).utility=10
        self.g.get_vertex(5).utility=5
        self.g.get_vertex(6).utility=15
        expect=[[0, -math.inf, math.inf],
                [1, -math.inf, math.inf],
                [3, 20, 20],
                [1, -math.inf, 20],
                [4, 10, 10],
                [1, 10, 10],
                [0, 10, math.inf],
                [2, -math.inf, math.inf],
                [5, 5, 5],
                [2, -math.inf, 5],
                [0, 10, 10]]
        self.assertListEqual(self.AL.miniMaxAlphaBeta(0,3,'alphaBeta'),expect)#node 6 is pruned
    def test_miniMaxAlphaBeta_exMiniMax(self):
        self.g.resetAllUtility()
        self.g.get_vertex(3).utility=20
        self.g.get_vertex(4).utility=1
        self.g.get_vertex(5).utility=10
        self.g.get_vertex(6).utility=4
        self.g.add_objEdge('a0')
        self.g.add_edge(2,'a0')
        self.g.delete_edge(2,5)
        self.g.delete_edge(2,6)
        self.g.get_vertex(5).probability=0.3
        self.g.get_vertex(6).probability=0.5
        self.g.add_objEdge_vert_connection('a0',5)#utility of node 5 =10, 10*0.3=3
        self.g.add_objEdge_vert_connection('a0',6)#utility of node 6 =4, 4*0.5=2
        #so now the total utility of action0 = 5
        expect=[[0, -math.inf, math.inf],
                [1, -math.inf, math.inf],
                [3, 20, 20],
                [1, -math.inf, 20],
                [4, 1, 1],
                [1, 1, 1],
                [0, 1, math.inf],
                [2, -math.inf, math.inf],
                [5, 10, 10],
                [6, 4, 4],
                [2, 5.0, 5.0],
                [0, 5.0, 5.0]]
        self.assertListEqual(self.AL.miniMaxAlphaBeta(0,3,'exMiniMax'),expect)
        self.g.add_edge(2,5)
        self.g.add_edge(2,6)
        self.g.delete_objEdge('a0')
    def test_generateProbabilityTable(self):
        self.g.add_edge(1,2)
        self.g.add_edge(1,5)
        self.g.add_edge(4,5)
        self.AL.generateProbabilityTable()
        expect={2: '[0, 1] : P',
                        'TT': [0,0],
                        'TF': [0,0],
                        'FT': [0,0],
                        'FF': [0,0]}
        self.assertDictEqual(self.g.get_vertex(2).probabilityTable,expect)
        expect={5: '[1, 2, 4] : P',
                        'TTT': [0,0],
                        'TTF': [0,0],
                        'TFT': [0,0],
                        'TFF': [0,0],
                        'FTT': [0,0],
                        'FTF': [0,0],
                        'FFT': [0,0],
                        'FFF': [0,0]}
        self.assertDictEqual(self.g.get_vertex(5).probabilityTable,expect)
        self.g.delete_edge(1,2)
        self.g.delete_edge(1,5)
        self.g.delete_edge(4,5)
    def test_simulateData(self):
        g=Linking.Graph()
        for i in range(5):
            g.add_vertex(i)
            g.get_vertex(i).probability=0.5#assume all probability=0.5
        g.add_edge(0,2)
        g.add_edge(1,2)
        g.add_edge(1,3)
        g.add_edge(2,4)
        al=Algorithms.algorithms(g.vert_dict)
        al.generateProbabilityTable()
        al.simulateData(10000)
        v=g.get_vertex(2).probabilityTable['TT'][0]
        self.assertTrue(v>0.115 and v<0.135)#expect v = 0.125
        v=g.get_vertex(3).probabilityTable['T'][0]
        self.assertTrue(v>0.24 and v<0.26)#expect v = 0.25
        v=g.get_vertex(4).probabilityTable['T'][0]
        self.assertTrue(v>0.24 and v<0.26)#expect v = 0.25
        v=g.get_vertex(0).probabilityTable['T'][0]
        self.assertTrue(v>0.49 and v<0.51)#expect v = 0.5
        v=g.get_vertex(1).probabilityTable['T'][0]
        self.assertTrue(v>0.49 and v<0.51)#expect v = 0.5
