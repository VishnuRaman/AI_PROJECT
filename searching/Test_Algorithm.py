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
    def test_bdfs_dfs_dif_Cost(self):
        g=Linking.Graph()
        for i in range(7):
            g.add_vertex(i)
        g.add_edge(0,2,2)
        g.add_edge(0,1,1)
        g.add_edge(1,4,4)
        g.add_edge(1,3,1)
        g.add_edge(2,6,1)
        g.add_edge(2,5,1)
        g.add_edge(2,4,2)
        al=Algorithms.algorithms(g.vert_dict)
        self.assertListEqual([0, 2, 4],al.ucsAStar(0,4,'UCS'))
    def test_ucsAStar_ucs(self):
        #UCS
        self.assertEqual([0,1,4],self.AL.ucsAStar(0,4,'UCS'))#Test UCS final path
        qsExpect=[[0, [1, 2], [1, 1]],
                  [1, [2, 3, 4], [1, 2, 2]],
                  [2, [3, 4, 5, 6], [2, 2, 2, 2]],
                  [3, [4, 5, 6], [2, 2, 2]],
                  [4, [5, 6], [2, 2]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test UCS qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test UCS visitedLog
    def test_ucsAStar_aStar(self):
        #A* (manual heuristic)
        self.g.get_vertex(1).heuristic=1
        self.g.get_vertex(3).heuristic=1
        self.assertEqual([0,1,4],self.AL.ucsAStar(0,4,'aStar'))#Test A* final path
        qsExpect=[[0, [2, 1], [1, 2]], [2, [1, 5, 6], [2, 2, 2]], [1, [5, 6, 4, 3], [2, 2, 3, 4]], [5, [6, 4, 3], [2, 3, 4]], [6, [4, 3], [3, 4]], [4, [3], [4]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test A* qsLog
        visitedExpect=[[0], [0, 2], [0, 2, 1], [0, 2, 1, 5], [0, 2, 1, 5, 6], [0, 2, 1, 5, 6, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test A* visitedLog
        self.g.resetAllHeuristic()
        #A* (default heuristic=0)
        self.assertEqual([0,1,4],self.AL.ucsAStar(0,4,'aStar'))#Test A* final path
        qsExpect=[[0, [1, 2], [1, 1]], [1, [2, 3, 4], [1, 2, 2]], [2, [3, 4, 5, 6], [2, 2, 2, 2]], [3, [4, 5, 6], [2, 2, 2]], [4, [5, 6], [2, 2]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test A* qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test A* visitedLog
    def test_bdfs_bfs_iter(self):
        #BFS
        self.assertEqual([0,1,4],self.AL.iterative(0,4,'BFS',3))#Test BFS final path
        qsExpect=[[0, [1, 2]], [1, [2]], [2, []], [0, [1, 2]], [1, [2, 3, 4]], [2, [3, 4, 5, 6]], [3, [4, 5, 6]], [4, [5, 6]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test BFS qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 2], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test BFS visitedLog
    def test_bdfs_dfs_iter(self):
        #DFS
        self.assertEqual([0,2,5],self.AL.iterative(0,5,'DFS',3))#Test DFS final path
        qsExpect=[[0, [1, 2]], [2, [1]], [1, []],[0, [1, 2]], [2, [1, 5, 6]], [6, [1, 5]], [5, [1]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test DFS qsLog
        visitedExpect=[[0], [0, 2], [0, 2, 1], [0], [0, 2], [0, 2, 6], [0, 2, 6, 5]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test DFS visitedLog
    def test_ucsAStar_ucs_iter(self):
        #UCS
        self.assertEqual([0,1,4],self.AL.iterative(0,4,'UCS',3))#Test UCS final path
        qsExpect=[[0, [1, 2], [1, 1]], [1, [2], [1]], [2, [], []], [0, [1, 2], [1, 1]], [1, [2, 3, 4], [1, 2, 2]], [2, [3, 4, 5, 6], [2, 2, 2, 2]], [3, [4, 5, 6], [2, 2, 2]], [4, [5, 6], [2, 2]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test UCS qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 2], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test UCS visitedLog
    def test_ucsAStar_aStar_iter(self):
        #A* (manual heuristic)
        self.g.get_vertex(1).heuristic=1
        self.g.get_vertex(3).heuristic=1
        self.assertEqual([0,1,4],self.AL.iterative(0,4,'aStar',3))#Test A* final path
        qsExpect=[[0, [2, 1], [1, 2]], [2, [1], [2]], [1, [], []], [0, [2, 1], [1, 2]], [2, [1, 5, 6], [2, 2, 2]], [1, [5, 6, 4, 3], [2, 2, 3, 4]], [5, [6, 4, 3], [2, 3, 4]], [6, [4, 3], [3, 4]], [4, [3], [4]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test A* qsLog
        visitedExpect=[[0], [0, 2], [0, 2, 1], [0], [0, 2], [0, 2, 1], [0, 2, 1, 5], [0, 2, 1, 5, 6], [0, 2, 1, 5, 6, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test A* visitedLog
        self.g.resetAllHeuristic()
        #A* (default heuristic=0)
        self.assertEqual([0,1,4],self.AL.iterative(0,4,'aStar',3))#Test A* final path
        qsExpect=[[0, [1, 2], [1, 1]], [1, [2], [1]], [2, [], []], [0, [1, 2], [1, 1]], [1, [2, 3, 4], [1, 2, 2]], [2, [3, 4, 5, 6], [2, 2, 2, 2]], [3, [4, 5, 6], [2, 2, 2]], [4, [5, 6], [2, 2]]]
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
        qsExpect=[[0, [1, 3], [1, 1]], [1, [3, 2, 4], [1, 2, 2]], [3, [2, 4, 6], [2, 2, 2]], [2, [4, 6, 5], [2, 2, 3]], [4, [6, 5], [2, 3]]]
        self.assertEqual(qsExpect,self.AL_gd.getQsLog())#Test UCS qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 3], [0, 1, 3, 2], [0, 1, 3, 2, 4]]
        self.assertEqual(visitedExpect,self.AL_gd.getVisitedLog())#Test UCS visitedLog
    def test_ucsAStar_aStar_grid(self):
        #A* (getManhattanDist)
        self.gd.setManhattanDist(4)
        self.assertEqual([0,1,4],self.AL_gd.ucsAStar(0,4,'aStar'))#Test A* final path
        qsExpect=[[0, [1, 3], [2, 2]], [1, [3, 4, 2], [2, 3, 5]], [3, [4, 2, 6], [3, 5, 5]], [4, [2, 6], [5, 5]]]
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
        qsExpect=[[0, [1, 3], [1, 1]], [1, [3], [1]], [3, [], []], [0, [1, 3], [1, 1]], [1, [3, 2, 4], [1, 2, 2]], [3, [2, 4, 6], [2, 2, 2]], [2, [4, 6], [2, 2]], [4, [6], [2]], [6, [], []]]
        self.assertEqual(qsExpect,self.AL_gd.getQsLog())#Test UCS qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 3], [0], [0, 1], [0, 1, 3], [0, 1, 3, 2], [0, 1, 3, 2, 4], [0, 1, 3, 2, 4, 6]]
        self.assertEqual(visitedExpect,self.AL_gd.getVisitedLog())#Test UCS visitedLog
    def test_ucsAStar_aStar_iter_grid(self):
        #A* (getManhattanDist)
        self.gd.setManhattanDist(4)
        self.assertEqual([0,1,4],self.AL_gd.iterative(0,4,'aStar',it=3))#Test A* final path
        qsExpect=[[0, [1, 3], [2, 2]], [1, [3], [2]], [3, [], []], [0, [1, 3], [2, 2]], [1, [3, 4, 2], [2, 3, 5]], [3, [4, 2, 6], [3, 5, 5]], [4, [2, 6], [5, 5]]]
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
        self.assertListEqual(self.AL.finalPath,[0, 1, 4])

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
        self.assertListEqual(self.AL.finalPath,[0, 2, 5])
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
        self.assertListEqual(self.AL.finalPath,[0, 1, 4])
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
        self.g.add_objEdge_vert_connection('a0',5,0.3)#utility of node 5 =10, 10*0.3=3
        self.g.add_objEdge_vert_connection('a0',6,0.5)#utility of node 6 =4, 4*0.5=2
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
        self.assertListEqual(self.AL.finalPath,[0, 2])
        self.g.add_edge(2,5)
        self.g.add_edge(2,6)
        self.g.delete_objEdge('a0')
    def test_generateProbabilityTable(self):
        self.g.add_edge(1,2)
        self.g.add_edge(1,5)
        self.g.add_edge(4,5)
        self.AL.generateProbabilityTable()
        expect={2: [0, 1],
                        'TT': [0,0,0,0],
                        'TF': [0,0,0,0],
                        'FT': [0,0,0,0],
                        'FF': [0,0,0,0]}
        self.assertDictEqual(self.g.get_vertex(2).probabilityTable,expect)
        expect={5: [1, 2, 4],
                        'TTT': [0,0,0,0],
                        'TTF': [0,0,0,0],
                        'TFT': [0,0,0,0],
                        'TFF': [0,0,0,0],
                        'FTT': [0,0,0,0],
                        'FTF': [0,0,0,0],
                        'FFT': [0,0,0,0],
                        'FFF': [0,0,0,0]}
        self.assertDictEqual(self.g.get_vertex(5).probabilityTable,expect)
        self.g.delete_edge(1,2)
        self.g.delete_edge(1,5)
        self.g.delete_edge(4,5)
    def test_simulateData(self):
        g=Linking.Graph()
        for i in range(5):
            g.add_vertex(i)
        #    0    1
        #       \ /  \
        #        2   3
        #       /
        #      4
        g.add_edge(0,2)
        g.add_edge(1,2)
        g.add_edge(1,3)
        g.add_edge(2,4)
        al=Algorithms.algorithms(g.vert_dict)
        al.generateProbabilityTable()
        al.setProbabilityTable(0,'T',0.1)
        al.setProbabilityTable(1,'T',0.5)
        al.setProbabilityTable(2,'TT',1)
        al.setProbabilityTable(2,'TF',1)
        al.setProbabilityTable(2,'FT',0.5)
        al.setProbabilityTable(2,'FF',0.01)
        al.setProbabilityTable(3,'T',0.8)
        al.setProbabilityTable(3,'F',0.01)
        al.setProbabilityTable(4,'T',0.1)
        al.setProbabilityTable(4,'F',0.01)
        al.simulateData(10000)
        v=g.get_vertex(0).probabilityTable['T'][0]#node 0
        self.assertAlmostEqual(v,0.1,1)#expect v =0.1
        v=g.get_vertex(1).probabilityTable['T'][0]#node 1
        self.assertAlmostEqual(v,0.5,1)#expect v = 0.5
        v=g.get_vertex(2).probabilityTable['TT'][0]#node 2
        self.assertAlmostEqual(v,1,1)#expect v =1
        v=g.get_vertex(3).probabilityTable['T'][0]#node 3
        self.assertAlmostEqual(v,0.8,1)#expect v = 0.8
        v=g.get_vertex(4).probabilityTable['T'][0]#node 4
        self.assertAlmostEqual(0.1,v,1)#expect v = 0.1

    def test_setProbabilityTable(self):
        g=Linking.Graph()
        for i in range(5):
            g.add_vertex(i)
        #    0    1
        #       \ /  \
        #        2   3
        #       /
        #      4
        g.add_edge(0,2)
        g.add_edge(1,2)
        g.add_edge(1,3)
        g.add_edge(2,4)
        al=Algorithms.algorithms(g.vert_dict)
        al.generateProbabilityTable()
        al.setProbabilityTable(0,'T',0.1)
        al.setProbabilityTable(1,'T',0.5)
        al.setProbabilityTable(2,'TT',1)
        al.setProbabilityTable(2,'TF',1)
        al.setProbabilityTable(2,'FT',0.5)
        al.setProbabilityTable(2,'FF',0.01)
        al.setProbabilityTable(3,'T',0.8)
        al.setProbabilityTable(3,'F',0.01)
        al.setProbabilityTable(4,'T',0.1)
        al.setProbabilityTable(4,'F',0.01)
        v=g.get_vertex(2).probabilityTable['TT'][3]#node 2
        self.assertTrue(v==1)#expect v =1
        v=g.get_vertex(3).probabilityTable['T'][3]#node 3
        self.assertTrue(v==0.8)#expect v = 0.8
        v=g.get_vertex(4).probabilityTable['T'][3]#node 4
        self.assertTrue(v==0.1)#expect v = 0.1
        v=g.get_vertex(0).probabilityTable['T'][3]#node 0
        self.assertTrue(v==0.1)#expect v = 0.1
        v=g.get_vertex(1).probabilityTable['T'][3]#node 1
        self.assertTrue(v==0.5)#expect v = 0.5

    def test_setKnownPT(self):
        g=Linking.Graph()
        for i in range(5):
            g.add_vertex(i)
        #    0    1
        #       \ /  \
        #        2   3
        #       /
        #      4
        g.add_edge(0,2)
        g.add_edge(1,2)
        g.add_edge(1,3)
        g.add_edge(2,4)
        al=Algorithms.algorithms(g.vert_dict)
        al.generateProbabilityTable()
        al.setKnownPT(0,'T',0.1)
        al.setKnownPT(1,'T',0.5)
        al.setKnownPT(2,'TT',1)
        al.setKnownPT(2,'TF',1)
        al.setKnownPT(2,'FT',0.5)
        al.setKnownPT(2,'FF',0.01)
        al.setKnownPT(3,'T',0.8)
        al.setKnownPT(3,'F',0.01)
        al.setKnownPT(4,'T',0.1)
        al.setKnownPT(4,'F',0.01)
        v=g.get_vertex(2).probabilityTable['TT'][0]#node 2
        self.assertTrue(v==1)#expect v =1
        v=g.get_vertex(3).probabilityTable['T'][0]#node 3
        self.assertTrue(v==0.8)#expect v = 0.8
        v=g.get_vertex(4).probabilityTable['T'][0]#node 4
        self.assertTrue(v==0.1)#expect v = 0.1
        v=g.get_vertex(0).probabilityTable['T'][0]#node 0
        self.assertTrue(v==0.1)#expect v = 0.1
        v=g.get_vertex(1).probabilityTable['T'][0]#node 1
        self.assertTrue(v==0.5)#expect v = 0.5
    def test_generatePriorProbability(self):
        g=Linking.Graph()
        for i in range(5):
            g.add_vertex(i)
        #    0    1
        #       \ /  \
        #        2   3
        #       /
        #      4
        g.add_edge(0,2)
        g.add_edge(1,2)
        g.add_edge(1,3)
        g.add_edge(2,4)
        al=Algorithms.algorithms(g.vert_dict)
        al.generateProbabilityTable()
        al.setKnownPT(0,'T',0.1)
        al.setKnownPT(1,'T',0.5)
        al.setKnownPT(2,'TT',1)
        al.setKnownPT(2,'TF',1)
        al.setKnownPT(2,'FT',0.5)
        al.setKnownPT(2,'FF',0.01)
        al.setKnownPT(3,'T',0.8)
        al.setKnownPT(3,'F',0.01)
        al.setKnownPT(4,'T',0.1)
        al.setKnownPT(4,'F',0.01)
        al.generatePriorProbability()
        self.assertTrue(g.get_vertex(0).probability==0.1)
        self.assertTrue(g.get_vertex(1).probability==0.5)
        self.assertTrue(g.get_vertex(2).probability==0.3295)
        self.assertTrue(g.get_vertex(3).probability==0.405)
        self.assertTrue(g.get_vertex(4).probability==0.039655)
    def test_query_simulating(self):
        g=Linking.Graph()
        for i in range(5):
            g.add_vertex(i)
        #    0    1
        #       \ /  \
        #        2   3
        #       /
        #      4
        g.add_edge(0,2)
        g.add_edge(1,2)
        g.add_edge(1,3)
        g.add_edge(2,4)
        al=Algorithms.algorithms(g.vert_dict)
        al.generateProbabilityTable()
        al.setProbabilityTable(0,'T',0.1)
        al.setProbabilityTable(1,'T',0.5)
        al.setProbabilityTable(2,'TT',1)
        al.setProbabilityTable(2,'TF',1)
        al.setProbabilityTable(2,'FT',0.5)
        al.setProbabilityTable(2,'FF',0.01)
        al.setProbabilityTable(3,'T',0.8)
        al.setProbabilityTable(3,'F',0.01)
        al.setProbabilityTable(4,'T',0.1)
        al.setProbabilityTable(4,'F',0.01)
        al.simulateData(10000)

        obs={3:'T',4:'T'}
        self.assertTrue(math.fabs(al.query(obs,0)-0.17)<=0.1)
        self.assertTrue(math.fabs(al.query(obs,1)-1)<=0.1)
        self.assertTrue(math.fabs(al.query(obs,2)-0.92)<=0.1)
        self.assertTrue(math.fabs(al.query(obs,3)-1)<=0.1)
        self.assertTrue(math.fabs(al.query(obs,4)-1)<=0.1)
        # print(al.refreshP(obs))
    def test_query_known(self):
        g=Linking.Graph()
        for i in range(5):
            g.add_vertex(i)
        #    0    1
        #       \ /  \
        #        2   3
        #       /
        #      4
        g.add_edge(0,2)
        g.add_edge(1,2)
        g.add_edge(1,3)
        g.add_edge(2,4)
        al=Algorithms.algorithms(g.vert_dict)
        al.generateProbabilityTable()
        al.setKnownPT(0,'T',0.1)
        al.setKnownPT(1,'T',0.5)
        al.setKnownPT(2,'TT',1)
        al.setKnownPT(2,'TF',1)
        al.setKnownPT(2,'FT',0.5)
        al.setKnownPT(2,'FF',0.01)
        al.setKnownPT(3,'T',0.8)
        al.setKnownPT(3,'F',0.01)
        al.setKnownPT(4,'T',0.1)
        al.setKnownPT(4,'F',0.01)
        al.generatePriorProbability()
        obs={3:'T',4:'T'}
        expected={0: 0.1694628029147602,
                  1: 0.9958554837953809,
                  2: 0.9228191078724887,
                  3: 1,
                  4: 1}
        self.assertDictEqual(al.refreshP(obs),expected)
        obs={3:'T'}
        expected={0: 0.1, 1: 0.9876543209876543, 2: 0.5445555555555555, 3: 1, 4: 0.05900999999999999}
        self.assertDictEqual(al.refreshP(obs),expected)
        obs={3:'F',4:'F'}
        expected={0: 0.09244807952710092, 1: 0.16236679513583266, 2: 0.1692887479810971, 3: 0, 4: 0}
        self.assertDictEqual(al.refreshP(obs),expected)
        obs={3:'T',4:'F'}
        expected={0: 0.09564394945748625, 1: 0.9871400215612162, 2: 0.520834440323489, 3: 1, 4: 0}
        self.assertDictEqual(al.refreshP(obs),expected)
        obs={1:'T',3:'T',4:'F'}#3(true) is conditional independant
        expected={0: 0.09665052244976859, 1: 1, 2: 0.5263157894736843, 3: 1, 4: 0}
        self.assertDictEqual(al.refreshP(obs),expected)
        obs={1:'T',4:'F'}#3(not given) is conditional independant
        expected={0: 0.1597316508266113, 1: 1, 2: 0.5263157894736843, 3: 0.8, 4: 0}
        self.assertDictEqual(al.refreshP(obs),expected)
        obs={1:'T',3:'T',4:'F'}#3(False) is conditional independant
        expected={0: 0.09665052244976859, 1: 1, 2: 0.5263157894736843, 3: 1, 4: 0}
        self.assertDictEqual(al.refreshP(obs),expected)
        obs={}#empty
        expected={0: 0.1, 1: 0.5, 2: 0.3295, 3: 0.405, 4: 0.039655}
        self.assertDictEqual(al.refreshP(obs),expected)

    def test_markov(self):
        g=Linking.Graph()
        g.add_vertex('rainy')
        g.add_vertex('sunny')
        g.add_edge('rainy','sunny',0.5)
        g.add_edge('rainy','rainy',0.5)
        g.add_edge('sunny','rainy',0.1)
        g.add_edge('sunny','sunny',0.9)
        g.get_vertex('rainy').probability=1#initial probability
        g.get_vertex('sunny').probability=0#initial probability
        model=g.vert_dict

        gg=Linking.Graph()
        gg.add_vertex(0)
        gg.add_vertex(1)
        gg.add_vertex(2)
        gg.add_vertex(3)
        gg.add_edge(0,1)
        gg.add_edge(1,2)
        gg.add_edge(2,3)
        al=Algorithms.algorithms(gg.vert_dict)
        expected={0: {'rainy': 1, 'sunny': 0},
                  1: {'rainy': 0.5, 'sunny': 0.5},
                  2: {'rainy': 0.3, 'sunny': 0.7},
                  3: {'rainy': 0.21999999999999997, 'sunny': 0.78}}
        self.assertDictEqual(al.markov(model,0),expected)

        expected={1: {'rainy': 1, 'sunny': 0},
                  2: {'rainy': 0.5, 'sunny': 0.5},
                  3: {'rainy': 0.3, 'sunny': 0.7}}
        self.assertDictEqual(al.markov(model,1),expected)

    def test_hiddenMarkov(self):
        g=Linking.Graph()
        g.add_vertex('rainy')
        g.add_vertex('sunny')
        g.add_vertex('hear')
        g.add_vertex('not')
        #transition probability
        g.add_edge('rainy','sunny',0.5)
        g.add_edge('rainy','rainy',0.5)
        g.add_edge('sunny','rainy',0.1)
        g.add_edge('sunny','sunny',0.9)
        #emission probability
        g.add_edge('rainy','hear',0.7)
        g.add_edge('rainy','not',0.3)
        g.add_edge('sunny','hear',0.2)
        g.add_edge('sunny','not',0.8)
        #initial probability
        g.get_vertex('rainy').probability=0.5
        g.get_vertex('sunny').probability=0.5
        model=g.vert_dict

        gg=Linking.Graph()
        #node
        gg.add_vertex(0)
        gg.add_vertex(1)
        gg.add_vertex(2)
        gg.add_vertex(3)
        #obs
        gg.add_vertex(4)
        gg.add_vertex(5)
        gg.add_vertex(6)

        gg.add_edge(0,1)
        gg.add_edge(1,2)
        gg.add_edge(2,3)
        gg.add_edge(0,4)#obs
        gg.add_edge(1,5)
        gg.add_edge(2,6)
        al=Algorithms.algorithms(gg.vert_dict)

        obs={4:'hear', 5:'hear', 6:'not'}
        states=['rainy','sunny']

        expected={0: {'rainy': 0.7777777777777778, 'sunny': 0.22222222222222227},
                  1: {'rainy': 0.7095890410958903, 'sunny': 0.2904109589041096},
                  2: {'rainy': 0.18936697454381615, 'sunny': 0.8106330254561839},
                  3: {'rainy': 0.17574678981752645, 'sunny': 0.8242532101824737}}
        # print(al.hiddenMarkov(model,0,obs,states))
        self.assertDictEqual(al.hiddenMarkov(model,0,obs,states),expected)

    def test_valueIteration(self):
        g=Linking.Grid(2,2)
        g.grid_dict[0].reward=-4
        g.grid_dict[1].utility=100
        g.grid_dict[1].reward=100
        g.grid_dict[2].utility=-100
        g.grid_dict[2].reward=-100
        g.setObstacle(3)
        al=Algorithms.algorithms(g.grid_dict)

        action={'forward':0.8, 'left':0.1, 'right':0.1}
        discount=0.9

        expexted={0: 64.83478199000001, 1: 100, 2: -100, 3: 0}
        # print(al.valueIteration(discount,action,g))
        self.assertDictEqual(al.valueIteration(discount,action,g),expexted)
        #another test
        g=Linking.Grid(4,3)
        for i in g.grid_dict:
            if i != 5:
                g.grid_dict[i].reward=-4
        g.grid_dict[3].utility=100
        g.grid_dict[3].reward=100
        g.grid_dict[7].utility=-100
        g.grid_dict[7].reward=-100
        g.setObstacle(5)
        al=Algorithms.algorithms(g.grid_dict)

        action={'forward':0.8, 'left':0.1, 'right':0.1}
        discount=0.9

        expexted={0: 50.94115412930875,
                  1: 64.95855729696827,
                  2: 79.5362031683467,
                  3: 100,
                  4: 39.85041277059019,
                  5: 0,
                  6: 48.6439148544741,
                  7: -100,
                  8: 29.64382885103273,
                  9: 25.391792612055916,
                  10: 34.476553020311734,
                  11: 12.99228937944113}
        # print(al.valueIteration(discount,action,g))
        self.assertDictEqual(al.valueIteration(discount,action,g),expexted)