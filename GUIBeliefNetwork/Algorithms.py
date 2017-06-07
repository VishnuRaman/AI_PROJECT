import math, numpy

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
            vertex = path[-1]
            # path found
            if vertex == goal:
                return path
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            elif vertex not in visited:
                for adjacent in self.graph.get(vertex, []):
                    new_path = list(path)
                    new_path.append(adjacent)
                    queue.append(new_path)
                    visited.add(vertex)


    def dfs(self,node, start, goal):
        if node == goal:
            return [node]
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


