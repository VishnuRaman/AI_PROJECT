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
                        print(queue)


    def dfs(self, start, goal):
        visited = set()
        stack = [(start,[start])]

        while stack:
            (node, path) = stack.pop()
            if node not in visited:
                visited.add(node)
                if node == goal:
                    return path
                for adj in self.graph[node]:
                    if adj not in visited :
                        stack.append((adj, path + [adj]))
                        print(stack)


# LK=Linking.Graph()
# LK.add_vertex(0)
# LK.add_vertex(1)
# LK.add_vertex(2)
# LK.add_vertex(3)
# LK.add_vertex(4)
# LK.add_vertex(5)
# LK.add_vertex(6)
# LK.add_edge(0,1,1)
# LK.add_edge(0,2,1)
# LK.add_edge(1,3,1)
# LK.add_edge(1,4,1)
# LK.add_edge(4,5,1)
# LK.add_edge(2,6,1)
# AL=algorithms(LK.vert_dict)

# for v in LK.vert_dict:
#     print(str(LK.vert_dict[v].get_id())+' is connected to '+str([g for g in LK.vert_dict[v]]))
# print(AL.bfs(0,5))
# print(AL.dfs(0,5))