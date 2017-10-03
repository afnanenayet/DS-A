# depth first search implemented in Python3
# note that graphs are represented by a dictionary - the key is the node 
# and the value is a set of neighbors

class Graph:
    def __init__(self, node_dict):
        self.visited = set()
        self.nodes = node_dict
        self.parents = dict()

def dfs(graph, source, target):
    """ Depth first search with a queue
    returns the path from source to target.
    Depth first search is a recursive algorithm that starts on some "source" 
    node. It keeps track of each visited node, and visits every unvisited node 
    adjacent to the current node recusively. 
    :type graph: dict
    :type target: int
    :rtype: bool """

    graph.visited.add(source)

    if source == target:
        print("Found target")
    else:
        for neighbor in graph.nodes[source]:
            if neighbor not in graph.visited:
                graph.parents[neighbor] = source
                dfs(graph, neighbor, target)


def path_helper(parent_map, src, dest):
    """ constructs a list with the desired path
    :type parent_map: dict
    :rtype: list """

    stack = []
    stack.append(src)

    while stack[len(stack)-1] != dest:
        stack.append(graph.parent_map[stack[len(stack)-1]])

    return stack


# test
nodes = dict()
nodes[1] = set([2, 4])
nodes[2] = set([1, 3, 5])
nodes[4] = set([1])
nodes[5] = set([2, 6])
nodes[3] = set([2, 6])
graph = Graph(nodes)
parents = dict()

dfs(graph, 1, 6)
print(graph.parents)
print(path_helper(graph.parents, 1, 6))
