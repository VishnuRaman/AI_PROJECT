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


def Bfs(graph, start, end):
    # keeps track of all paths to be checked
    queue = [[start]]
    # keeps track of visited nodes
    visited = set()

    # keeps looping until all possible paths are checked
    while queue:
        # Gets the first path in the queue
        path = queue.pop(0)

        # Gets the last node in the path
        node = path[-1]

        # Checks if we got to the end
        if node == end:
            return path
        # We check if the current node is already in the visited nodes set in order not to recheck it
        elif node not in visited:

            # enumerate all adjacent nodes, construct a new path and push it into the queue

            for m in graph.vert_dict:

                for n in graph.vert_dict[m].adjacent:
                    new_path = list(path)
                    new_path.append(n)
                    #print(list(new_path))
                    queue.append(new_path)

                    # Mark the node as visited
                visited.add(node)


LK = Linking.Graph()
LK.add_vertex(0)
LK.add_vertex(1)
LK.add_vertex(2)
LK.add_vertex(3)
LK.add_vertex(4)
LK.add_edge(0, 1, 1)
LK.add_edge(0, 2, 1)
LK.add_edge(1, 3, 1)
LK.add_edge(1, 4, 1)

for v in list(LK):
    print (str(v.get_id()) + str(LK.vert_dict[v.get_id()]))

# print(list(Bfs(LK, 0, 4)))

print(Bfs(LK, 0, 4))
