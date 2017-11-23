# dijkstra.py
# Afnan Enayet

def dijkstra(graph, src):
    """ Dijkstra's algorithm with a regular queue
    :type graph: dict
    :type src: int
    """

    dist = dict()  # the distances from src to dist[x]
    prev = dict()  # the previous node for node x
    visited = set()
    q = list()

    # Initialize Dijkstra
    for vertex in graph.keys():
        dist[vertex] = INT.MAX
        prev[vertex] = None

    q.append(src)

    while len(q) > 0:
        # find vertex adj to q with min distance
        # TODO finish Dijkstra

    pass


# test
graph = dict()

