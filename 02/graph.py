
__all__ = ['Graph']

from abc import ABC, abstractmethod

class Graph(ABC):
    """ a (directed) graph as a collection of nodes and edges 
        # nodes are maintained in a dict of { name[hashable] : Info{} }
        # edges are maintained in a dict of { (name[hashable], name[hashable]) : Info{} }
    """

    @abstractmethod
    def __len__(self): 
        r""" returns the number of nodes """
        ...

    @abstractmethod
    def __iter__(self):
        r""" return an iterator over nodes """
        ...


    r"""
    with slice types,
        Edge `(key.start, key.stop)`                single edge in uni graph, all (multiplicy) edges in multi graph
        Edge `(key.start, key.stop, key.step)`      single edge in multi graph
    """

    @abstractmethod
    def __contains__(self, key):
        r""" use to check membership of key
        if `key` is 
            slice (non-hashable) - returns the Edge `(key.start, key.stop)`
            list  (non-hashable) - return the Edge `tuple(key)`
            Any   (hashable) -     return the Node `key`
        """
        ...

    @abstractmethod
    def __getitem__(self, key):
        r""" use to return the value of a key (read nodes and edges of a graph))
        if `key` is 
            slice (non-hashable) - returns the Edge `(key.start, key.stop)`
            Any   (hashable) -     return the Node `key`
        """
        ...

    @abstractmethod
    def __setitem__(self, key, value):
        r""" use to set the value of a key (add nodes and edges to graph)
        if `key` is 
            slice (non-hashable) - set the Edge `(key.start, key.stop)`
            Any   (hashable) -     set the Node `key`
        """
        ...

    @abstractmethod
    def __delitem__(self, key): 
        r""" use to remove the value of a key (remove nodes and edges from a graph)
        if `key` is 
            slice (non-hashable) - del the Edge `(key.start, key.stop)`
            Any   (hashable) -     del the Node `key` (and associated edges)
        """
        ...

    @abstractmethod
    def __add__(self, other):
        r""" use to add nodes and edges to the graph (operator +)
        `other` must be a list only (non-hashable)
        if `len(other)` 
            == 1 then `other` is a node - add the node (hashable) (use __setitem__)
            == 2 then `other` is an edge - add the edge (2-tuple) (use __setitem__)

        syntax: 
            graph + [node]
            graph + [node, node]
        """
        ...

    @abstractmethod
    def __sub__(self,  other):
        r""" use to remove nodes and edges from the graph (operator -)
        `other` must be a list only (non-hashable)
        if `len(other)` 
            == 1 then `other` is a node - remove the node (hashable) (use __delitem__)
            == 2 then `other` is an edge - remove the edge (2-tuple) (use __delitem__)
        
        syntax: 
            graph - [node]
            graph - [node, node]
        """
        ...
    
    @abstractmethod
    def __lt__(self, other): 
        r""" Nodes-out or Out-degree - returns the nodes that are sucessors of `other` (node-hashable)
             graph < node
        """
        ...

    @abstractmethod
    def __gt__(self, other): 
        r""" Nodes-in or In-degree - returns the nodes that are predecessor of `other` (node-hashable)
             graph > node
        """
        ...

    @abstractmethod
    def __lshift__(self, other): 
        r""" Edges-out - returns the edges that are sucessors of `other` ((node,node)-hashable)
             graph << node
        """
        ...

    @abstractmethod
    def __rshift__(self, other): 
        r""" Edges-in - returns the edges that are predecessor of `other` ((node,node)-hashable)
             graph >> node
        """
        ...

        # Remove associated edges in the adjacency matrix

    def _add_(self, other):
        if len(other) == 1:
            node = other[0]
            self.nodes[node] = {}
            self.adjacency_matrix[node] = {}
        elif len(other) == 2:
            edge = tuple(other)
            self.adjacency_matrix[edge[0]][edge[1]] = {}
            # Add edge to the adjacency matrix

    def _sub_(self, other):
        if len(other) == 1:
            node = other[0]
            del self.nodes[node]
            del self.adjacency_matrix[node]
        elif len(other) == 2:
            edge = tuple(other)
            del self.adjacency_matrix[edge[0]][edge[1]]
            # Remove edge from the adjacency matrix

    def _lt_(self, other):
        # Implement Nodes-out or Out-degree logic
        pass

    def _gt_(self, other):
        # Implement Nodes-in or In-degree logic
        pass

    def _lshift_(self, other):
        # Implement Edges-out logic
        pass

    def _rshift_(self, other):
        # Implement Edges-in logic
        pass