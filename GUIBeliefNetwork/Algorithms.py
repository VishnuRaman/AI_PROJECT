import math, numpy,Linking

class algorithms:
    def __init__(self,dict):
        self.graph = dict


    def bfs(self, start, goal):
        # maintain a queue of paths
        queue = []
        #push first path into the queue
        queue.append([start])

        visited = set()
        while queue:
            # gets the first path in the queue
            path = queue.pop(0)
            # gets the last node from the path
            for vertex in path:
                # path found
                if vertex == goal:
                    return path
                # enumerate all adjacent nodes, construct a new path and push it into the queue
                elif vertex not in visited:
                    for adj in self.graph[vertex]:
                        new_path = list(path)
                        new_path.append(adj)
                        queue.append(new_path)
                        visited.add(vertex)



    def dfs(self, start, goal):
        stack = [start]
        visited = set()
        while stack:
            (vertex, path ) = stack.pop()
            if vertex not in visited:
                if vertex == goal:
                    return path
                visited.add(vertex)
                for neighbour in self.graph[vertex]:
                    stack.append((neighbour, path + [neighbour]))



LK=Linking.Graph()
LK.add_vertex(0)
LK.add_vertex(1)
LK.add_vertex(2)
LK.add_vertex(3)
LK.add_vertex(4)
LK.add_edge(0,1,1)
LK.add_edge(0,2,1)
LK.add_edge(1,3,1)
LK.add_edge(1,4,1)
AL=algorithms(LK.vert_dict)

for v in LK.vert_dict:
    print(str(LK.vert_dict[v].get_id())+' is connected to '+str(LK.vert_dict[v]))
print(AL.bfs(0,3))