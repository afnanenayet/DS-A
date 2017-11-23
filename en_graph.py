# en_graph.py


class Node(object):
    """ A node class that holds the value of a node and stores its neighbors
    """

    def __init__(self, value, neighbors: set = None):
        """ initializes a value with a set of neighboss
        :param value: a value, can be anything
        :param neighbors: a set of nodes that are connected to this node
        """
        self.value = value

        if set is None:
            self.neighbors == set()
        else:
            # If arguments are invalid, throw error
            if not isinstance(neighbors, set):
                raise TypeError("neighbors must be a set of nodes")
            else:
                for node in neighbors:
                    if !isinstance(node, Node):
                        raise TypeError(
                            "set must contain all instances of Node class")
            self.neighbors = neighbors


class Edge(object):
    """ an edge object that can be weighted
    """

    def __init__(self, node: Node = None, neighbor: Node = None,
                 pair: tuple = None, weight=1):
        """ creates a directed edge object that can be initialized by either passing
        two edges in as arguments, or a tuple pair. If a node, neighbor, and pair are
        passed in, the node and neighbor will be used to construct the edge

        The edge will be constructed as (node, neighbor), or node -> neighbor
        :param node: the origin for the edge, must be a Node object
        :param neighbor: the outbound endpoint of the edge, must be a Node object
        :param pair: a tuple of the form (node, neighbor) that must have a length of 2
          and is mutually exclusive with node and neighbor params
        :param weight: (optional) weight of of the edge
        """
        # weight can be anything that Python can compare
        self.weight = weight

        # check that all variables are valid
        if isinstance(node, Node) and isinstance(neighbor, Node):
            (self.a, self.b) = (node, neighbor)
        elif isinstance(pair, tuple):
            # A pair must consist of two Node objects
            if len(tuple) == 2:
                if isinstance(pair[0], Node) and isinstance(pair[1], Node):
                    self.a = pair[0]
                    self.b = pair[1]
                else:
                    raise TypeError("values of pair need to be Node objects")
            else:
                raise ValueError("pair must contain two Nodes")
        else:
            raise TypeError("invalid arguments")


class Graph(object):
    """ A convenient graph class that allows for various ways of reading/writing

    nodes. Stores nodes as Node objects, and also stores nodes with adjacency
    list representations, as well as storing edges

    If the graph is undirected and unweighted:
        - the adjacency list will be a dictionary of the form {node : set(neighbors)}
        - note that neighbors will be imputed symmetrically for all nodes
        - if a node has a neighor, that node will be added as a neighbor to
        its neighbor
        - the edge list will be a set of sets of the form set(set(nodeA, nodeB))
        If the graph is undirected and weighted:
            - the adjacency list will be a dictionary of the form:
                {node : set(tuple(neighbor, weight))}
                - the edge list will have the following structure:
                    tuple(set(nodeA, nodeB), weight)
                    If the graph is directed and unweighted:
                        - adjacency list: dictionary{node: set(neighbors)}
                        - edge list: set(tuple(nodeA, nodeB))
    """

    def __init__(self, adj_edge, is_directed: bool=False):
        """ Initializes the graph with optional adjacency list or edge list
        node representations. Will only take one, not both
        :param directed: a boolean indicating whether the graph is directed
        :param weighted: a boolean indicating whether the graph is weighted
        :param node_edge: either a dictionary with an adjacency list, or a set
        of edges
        :returns: a Graph object
        """
        self.directed = directed
        self.edge_set = set()
        self.node_set = set()

        if not Node.verify_args():
            raise ValueError("invalid arguments")

        # if arguments are valid, construct the rest of the graph
        # representation
        using_adj_list = isinstance(adj_edge, dict)

        if using_adj_list:
            self._process_edge_set()
        else:
            self._process_adj_list()

    def _build_edge_set(self):
        """ Builds edge list from the adjacency list representation in the
        graph
        """
        for node in self.node_set:
            for neighbor in node.neighbors:
                self.edge_set.add(Edge(node, neighbor))

                if not self.is_directed:
                    self.edge_set.add(Edge(neighbor, node))

    def _build_adj_list(self):
        """ Builds an adjacency list representation from the edge list
        """
        for edge in self.edge_set:
            node = edge.a
            node.neighbors.add(edge.b)
            self.node_set.add(node)

            # add the symmetric relationship if it is undirected
            if not self.is_directed:
                edge.b.neighbors.add(node)
                self.node_set.add(edge.b)

    def add_node(node: Node):
        """ Adds a node to the graph
        :param node: the node to be added to the graph
        """
        self.node_set.add(node)

        for neighbor in node.neighbors:
            e = Edge(node, neighbor)
            self.edge_set.add(e)

    @staticmethod
    def verify_args(adj_edge, is_directed: bool) -> bool:
        """ returns whether arguments are valid
        :param adj_edge: a set or dict with the edges/nodes
        :param is_directed: a boolean indicating whether the graph is
        directed
        :returns: whether arguments are valid
        """
        # dict = adjacency list format
        # set = edge list format

        # verify types of arguments

        # Checking types in adjacency list
        if isinstance(adj_edge, dict):
            for node in dict:
                if not isinstance(node, Node):
                    return False
                if not isinstance(adj_edge[node], set):
                    return False
                else:
                    for node in adj_edge[node]:
                        if not isinstance(node, Node):
                            return False
        elif isinstance(adj_edge, set):  # checking edge set
            for edge in adj_edge:
                if not isinstance(edge, Edge):
                    return False
        return True  # if the graph passes all the checks

    def remove_node(self, node: Node) -> bool:
        """ Removes a node from the graph. Will return whether node was deleted
        from the graph
        """
        if node not in self.node_set:
            return False

        del self.node_set[node]

        # delete every edge that contains the node to be deleted
        for edge in self.edge_set:
            if edge.a == node or edge.b == node:
                del self.edge_set[edge]
        return True
