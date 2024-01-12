from graph import Graph

class Work(Graph):
    def __init__(self):
        self.nodes = {}
        self.adjacenecy_matrix = {}

    def __len__(self):
        return len(self.nodes)
    
    def __iter__(self):
        return iter(self.nodes)
    
    def __contains__(self, key):
        if(isinstance(key, slice)):
            if key.step is not None:
                return (key.start, key.stop, key.step) in self.adjacenecy_matrix
            return (key.start, key.stop) in self.adjacenecy_matrix
        elif isinstance(key, list):
            return tuple(key) in self.adjacenecy_matrix
        else:
            return key in self.nodes
    
    def __getitem__(self, key):
        if(isinstance(key, slice)):
            return self.adjacenecy_matrix[key.start, key.stop]
        else:
            return self.nodes[key]
    
    def __setitem__(self, key, value):
        if(isinstance(key, slice)):
            self.adjacenecy_matrix[key.start, key.stop] = value
        else:
            self.nodes[key] = value

    def __delitem__(self, key):
        if(isinstance(key, slice)):
            del self.adjacenecy_matrix[key.start, key.stop]
        else:
            del self.nodes[key]
        