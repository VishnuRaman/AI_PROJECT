import Linking
graph = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [10],
    4: [7, 8],
    5: [9, 10],
    7: [11, 12],
    11: [13]
}


def Bfs(graph_to_search, start, end):
    queue = [[start]]
    visited = set()

    while queue:
        # Gets the first path in the queue
        path = queue.pop(0)

        # Gets the last node in the path
        vertex = path[-1]

        # Checks if we got to the end
        if vertex == end:
            return path
        # We check if the current node is already in the visited nodes set in order not to recheck it
        elif vertex not in visited:
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            for m in graph_to_search.vert_dict:
                for n in graph_to_search.vert_dict[m].adjacent:
                    new_path = list(path)
                    new_path.append(n)
                    queue.append(new_path)

            # Mark the vertex as visited
                    visited.add(vertex)



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

print(list(Bfs(LK, 0, 4)))
