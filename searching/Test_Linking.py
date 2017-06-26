import unittest,Algorithms,pickle,Linking,os

class Test_linking(unittest.TestCase):


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
        self.assertEqual('dict_keys([0, 1, 2, 3, 4, 5])',str(v.get_connections()))
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
    def test_g_saveFile_and_loadFile_and_fileNames(self):
        g=Linking.Graph()
        newDict=g.vert_dict#create a vert_dict
        output = open('junk2'+'.pkl', 'wb')
        pickle.dump(newDict, output)#store it into disk
        output.close()
        self.assertTrue('junk2.pkl' in g.fileNames())# is there a file called junk2?
        os.remove('junk2.pkl')#now delete it
        self.assertFalse('junk2.pkl' in g.fileNames())# is there a file called junk2?

