

__all__ = ['binary_knapsack', 'max_flow']



#------------------------------------------------------------------------------
# [Q1] Solution
#------------------------------------------------------------------------------
from typing import List

def binary_knapsack(capacity:float, weights:List[float], costs:List[float]):
    ...

#------------------------------------------------------------------------------



#------------------------------------------------------------------------------
# [Q2] Solution
#------------------------------------------------------------------------------
from typing import Hashable as Node, SupportsFloat as Capacity

def max_flow(
    nodes:  set[Node],
    edges:  dict[tuple[Node],  Capacity],
    source: Node,
    sink:   Node,
): ...


#------------------------------------------------------------------------------
    

