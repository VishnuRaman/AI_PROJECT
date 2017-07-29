import unittest,Algorithms,pickle,Linking,os

class Test_linking(unittest.TestCase):

#For Vertex
    def test_v_check_neighbor_existed(self):
        v=Linking.Vertex(6)# vertex 6
        for i in range(6):# vertex 6 is connected to 0~5
            v.adjacent[i]=1
        for i in range(6):#is vertex 6 connected to 0~5 ?
            self.assertTrue(v.check_neighbor_existed(i))
    def test_v_add_neighbor(self):
        v=Linking.Vertex(0)# vertex 0
        v.add_neighbor(1)# vertex 0 is connected to 1
        v.add_neighbor(2)# vertex 0 is connected to 2
        self.assertTrue(v.check_neighbor_existed(1))#is vertex 0 connected to 1 ?
        self.assertTrue(v.check_neighbor_existed(2))#is vertex 0 connected to 2 ?
    def test_v_delete_neighbor(self):
        v=Linking.Vertex(0)
        for i in range(6):# vertex 0 is connected to 0~5
            v.adjacent[i]=1
        for i in range(3):
            v.delete_neighbor(i)
        for i in range(6):
            if(i<3):
                self.assertFalse(v.check_neighbor_existed(i))
            else:
                self.assertTrue(v.check_neighbor_existed(i))
    def test_v_get_connections(self):
        v=Linking.Vertex(0)
        for i in range(6):# vertex 0 is connected to 0~5
            v.adjacent[i]=1
        self.assertListEqual([0, 1, 2, 3, 4, 5],v.get_connections())
    def test_v_get_id(self):
        v=Linking.Vertex(0)
        self.assertTrue(v.get_id()==0)
        v=Linking.Vertex(7)
        self.assertTrue(v.get_id()==7)
    def test_v_get_weight(self):
        v=Linking.Vertex(0)
        for i in range(6):# vertex 0 is connected to 0~5
            v.adjacent[i]=i
        for i in range(6):
            self.assertTrue(v.get_weight(i)==i)

 #For Graph
    def test_g_add_vertex(self):
        g=Linking.Graph()
        g.add_vertex(0)#add vertex
        g.add_vertex(1)
        self.assertTrue(str(g.vert_dict[0].get_id())==str(0))#see if the vertex exist
        self.assertTrue(str(g.vert_dict[1].get_id())==str(1))
    def test_g_delete_vertex(self):
        g=Linking.Graph()
        g.add_vertex(0)
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_edge(0,1,1)#0 connect to 1
        g.add_edge(0,2,1)#0 connect to 2
        g.delete_vertex(2)#delete 2
        self.assertTrue(1 in g.vert_dict[0].adjacent.keys())#0 is connected to 1
        self.assertFalse(2 in g.vert_dict[0].adjacent.keys())#0 is not connected to 2
        self.assertTrue((0 in g.vert_dict.keys()))#vertex 0 exist
        self.assertTrue((1 in g.vert_dict.keys()))#vertex 1 exist
        self.assertFalse((2 in g.vert_dict.keys()))#vertex 2 not exist
    def test_g_get_vertex(self):
        g=Linking.Graph()
        v=Linking.Vertex(0)#create a vertex
        g.vert_dict[0]=v#store the vertex into vert_dict
        self.assertEqual(g.get_vertex(0),v)
    def test_g_add_edge(self):
        g=Linking.Graph()
        g.add_vertex(0)
        g.add_vertex(1)
        g.add_edge(0,1,1)
        self.assertTrue(1 in g.vert_dict[0].adjacent.keys())
        self.assertFalse(2 in g.vert_dict[0].adjacent.keys())
    def test_g_delete_edge(self):
        g=Linking.Graph()
        g.add_vertex(0)
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_edge(0,1,1)
        g.add_edge(0,2,1)
        g.delete_edge(0,2)
        self.assertTrue(1 in g.vert_dict[0].adjacent.keys())
        self.assertFalse(2 in g.vert_dict[0].adjacent.keys())
    def test_g_check_edge_existed(self):
        g=Linking.Graph()
        g.add_vertex(0)
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_edge(0,1,1)
        g.add_edge(0,2,1)
        self.assertTrue(g.check_edge_existed(0,1))
        self.assertTrue(g.check_edge_existed(0,2))
        g.delete_edge(0,2)
        self.assertTrue(g.check_edge_existed(0,1))
        self.assertFalse(g.check_edge_existed(0,2))
    def test_g_get_vertices(self):
        g=Linking.Graph()
        g.add_vertex(0)
        g.add_vertex(1)
        self.assertListEqual(g.get_vertices(),[0,1])
        g.add_vertex(2)
        self.assertListEqual(g.get_vertices(),[0,1,2])
    # def test_g_saveFile_and_loadFile_and_fileNames(self):
    #     g=Linking.Graph()
    #     g.saveFile('junk2')
    #     self.assertTrue('junk2_g.pkl' in g.fileNames())# is there a file called junk2?
    #     self.assertDictEqual(g.loadFile('junk2'),g.vert_dict)
    #     os.remove('junk2_g.pkl')#now delete it
    #     self.assertFalse('junk2_g.pkl' in g.fileNames())# is there a file called junk2?

    def test_g_resetAllHeuristic(self):
        g=Linking.Graph()
        g.add_vertex(0)
        g.add_vertex(1)
        g.get_vertex(0).heuristic=1
        g.get_vertex(1).heuristic=2
        g.resetAllHeuristic()
        self.assertTrue(g.vert_dict[0].heuristic==0)
        self.assertTrue(g.vert_dict[1].heuristic==0)
    def test_g_resetAllUtility(self):
        g=Linking.Graph()
        g.add_vertex(0)
        g.add_vertex(1)
        g.get_vertex(0).utility=2
        g.get_vertex(1).utility=3
        g.resetAllUtility()
        self.assertEqual(g.get_vertex(0).utility,0)
        self.assertEqual(g.get_vertex(1).utility,0)
    def test_g_add_objEdge(self):
        g=Linking.Graph()
        g.add_objEdge('a0')
        self.assertEqual(g.vert_dict['a0'].id,'a0')
    def test_g_add_objEdge_vert_connection(self):
        g=Linking.Graph()
        g.add_vertex(0)
        g.add_vertex(1)
        g.add_objEdge('a0')
        g.add_objEdge_vert_connection('a0',0,0.5)
        self.assertEqual(g.vert_dict['a0'].neighbor[0],0.5)
    def test_g_delete_objEdge_vert_connection(self):
        g=Linking.Graph()
        g.add_vertex(0)
        g.add_vertex(1)
        g.add_objEdge('a0')
        g.add_objEdge_vert_connection('a0',0,0.8)
        g.add_edge(0,1,3)
        g.delete_objEdge_vert_connection('a0',0)
        self.assertDictEqual(g.vert_dict['a0'].neighbor,{})#  empty
        self.assertDictEqual(g.vert_dict[0].adjacent,{1:3})
    def test_g_add_objEdge2(self):#for adding connection from node(as parent) to action(as chile)
        g=Linking.Graph()
        g.add_vertex(0)
        g.add_objEdge('a0')
        g.add_edge(0,'a0')
        self.assertDictEqual(g.vert_dict[0].adjacent,{'a0':1})


#For Grid
    def test_gd_init(self):
        gd=Linking.Grid(3,3)
        self.assertTrue(8 in gd.grid_dict.keys())
        self.assertEqual([i for i in gd.grid_dict[4].adjacent.keys()],[3,5,1,7])#the order doesn't matter
        self.assertEqual([i for i in gd.grid_dict[8].adjacent.keys()],[7,5])
    def test_gd_setWall(self):
        gd=Linking.Grid(3,3)
        self.assertTrue(4 in gd.grid_dict[3].adjacent.keys())#before setWall, they are connected to each other
        self.assertTrue(3 in gd.grid_dict[4].adjacent.keys())
        gd.setWall(3,4)
        self.assertFalse(4 in gd.grid_dict[3].adjacent.keys())#after setWall, they are not connected to each other
        self.assertFalse(3 in gd.grid_dict[4].adjacent.keys())
    def test_gd_breakWall(self):
        gd=Linking.Grid(3,3)
        gd.setWall(3,4)
        self.assertFalse(4 in gd.grid_dict[3].adjacent.keys())#before breakWall, they are not connected to each other
        self.assertFalse(3 in gd.grid_dict[4].adjacent.keys())
        gd.breakWall(3,4)
        self.assertTrue(4 in gd.grid_dict[3].adjacent.keys())#after breakWall, they are connected to each other
        self.assertTrue(3 in gd.grid_dict[4].adjacent.keys())
    def test_gd_physicalNeighbor(self):
        gd=Linking.Grid(3,3)
        self.assertListEqual(gd.physicalNeighbor(3),[0,6,4])
        gd.setWall(3,4)# the result won't be changed by adding a wall
        self.assertListEqual(gd.physicalNeighbor(3),[0,6,4])
    def test_gd_setObstacle(self):
        gd=Linking.Grid(3,3)
        for i in [1,7,3,5]:#before setObstacle, 4 is connecting to 1,7,3,5
            self.assertTrue(4 in gd.grid_dict[i].adjacent.keys())
            self.assertTrue(i in gd.grid_dict[4].adjacent.keys())
        gd.setObstacle(4)
        for i in [1,7,3,5]:#after setObstacle, they are not connected to each other
            self.assertFalse(4 in gd.grid_dict[i].adjacent.keys())
            self.assertFalse(i in gd.grid_dict[4].adjacent.keys())
    def test_gd_removeObstacle(self):
        gd=Linking.Grid(3,3)
        gd.setObstacle(4)
        for i in [1,7,3,5]:#before removeObstacle, they are not connected to each other
            self.assertFalse(4 in gd.grid_dict[i].adjacent.keys())
            self.assertFalse(i in gd.grid_dict[4].adjacent.keys())
        gd.removeObstacle(4)
        for i in [1,7,3,5]:#after removeObstacle, 4 is connecting to 1,7,3,5
            self.assertTrue(4 in gd.grid_dict[i].adjacent.keys())
            self.assertTrue(i in gd.grid_dict[4].adjacent.keys())
    def test_gd_setGridWeight(self):
        gd=Linking.Grid(3,3)
        self.assertTrue(gd.grid_weight[6]==1)#cost of unit grid6 is 1 (default)
        self.assertTrue(gd.grid_dict[3].adjacent[6]==1)#the weight of physical neighbors connecting to it is also 1
        self.assertTrue(gd.grid_dict[7].adjacent[6]==1)
        gd.setGridWeight(6,2)#after setting cost to 2
        self.assertTrue(gd.grid_weight[6]==2)#cost of unit grid6 is 2
        self.assertTrue(gd.grid_dict[3].adjacent[6]==2)#the weight of physical neighbors connecting to it is also 2
        self.assertTrue(gd.grid_dict[7].adjacent[6]==2)
    def test_gd_setManhattanDist(self):
        gd=Linking.Grid(3,3)
        dict={0:1,1:0,2:1,
              3:2,4:1,5:2,
              6:3,7:2,8:3}
        gd.setManhattanDist(1)
        for i in range(9):
            self.assertEqual(gd.grid_dict[i].heuristic,dict[i])
        dict={0:2,1:1,2:2,
              3:1,4:0,5:1,
              6:2,7:1,8:2}
        gd.setManhattanDist(4)
        for i in range(9):
            self.assertEqual(gd.grid_dict[i].heuristic,dict[i])
    # def test_gd_saveFile_and_loadFile_and_fileNames(self):
    #     gd=Linking.Grid(3,3)
    #     gd.saveFile('junk2')
    #     self.assertTrue(gd.loadFile('junk2')[3].id==gd.grid_dict[3].id)
    #     self.assertTrue('junk2_gd.pkl' in gd.fileNames())# is there a file called junk2?
    #     os.remove('junk2_gd.pkl')#now delete it
    #     self.assertFalse('junk2_gd.pkl' in gd.fileNames())# is there a file called junk2?

    def test_gd_resetAllUtility(self):
        gd=Linking.Grid(3,3)
        gd.grid_dict[0].utility=3
        gd.grid_dict[2].utility=4
        gd.resetAllUtility()
        self.assertEqual(gd.grid_dict[0].utility,0)
        self.assertEqual(gd.grid_dict[2].utility,0)