import math, numpy

class algorithms:
    def __init__(self,dict):
        self.graph = dict


    def bfs(self, start, goal):
        # maintain a queue of paths
        queue = []
        #push first path into the queue
        queue.append([start])
        while queue:
            # gets the first path in the queue
            path = queue.pop(0)
            # gets the last node from the path
            node = path[-1]
            # path found
            if node == goal:
                return path
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            for adjacent in self.graph.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)


    def dfs(self,current, start, goal):
        if current == goal:
            return [current]
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


