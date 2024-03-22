__all__ = ['binary_knapsack', 'max_flow']

#------------------------------------------------------------------------------
# [Q1] Solution
#------------------------------------------------------------------------------
from typing import List, Tuple, Hashable as Node, SupportsFloat as Capacity
import numpy as np
from scipy.optimize import linprog

def binary_knapsack(capacity: float, weights: List[float], costs: List[float]) -> List[int]:
    '''
    Solves the binary knapsack problem using linear programming.

    Parameters:
    - capacity (float): Total capacity of the knapsack.
    - weights (List[float]): List of weights for each item.
    - costs (List[float]): List of costs for each item.

    Returns:
    - List[int]: List of binary decisions indicating if each item is added to the knapsack (1) or not (0).
    '''
    num_items = len(weights)
    
    # Coefficients for the objective function (negative costs for maximization)
    c = [-costs[i] for i in range(num_items)]
    
    # Coefficients for the inequality constraint (capacity constraint)
    A_ub = np.array([weights])
    b_ub = np.array([capacity])
    
    # Bounds for each variable (binary decision variables)
    bounds = [(0, 1) for _ in range(num_items)]

    arr = [1] * num_items
    
    # Solve the linear programming problem
    result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs', integrality=arr)
    
    # Extract the binary decisions (rounding the solution)
    decisions = [int(round(x)) for x in result.x]
    
    return decisions

#------------------------------------------------------------------------------
# [Q2] Solution
#------------------------------------------------------------------------------

def max_flow(
    nodes: set[Node],
    edges: dict[Tuple[Node, Node], Capacity],
    source: Node,
    sink: Node,
) -> Tuple[List[float], List[List[float]], List[float], List[List[float]], List[float], List[Tuple[float, float]]]:
    '''
    Formulate the maximum flow problem as a Linear Programming (LP) problem.

    Parameters:
    - nodes (set[Node]): Set of nodes in the flow network.
    - edges (dict[Tuple[Node, Node], Capacity]): Dictionary of edges with capacities.
    - source (Node): Source node of the flow network.
    - sink (Node): Sink node of the flow network.

    Returns:
    - c (List[float]): Coefficients for the objective function.
    - A_ub (List[List[float]]): Coefficients matrix for inequality constraints.
    - b_ub (List[float]): Right-hand side of inequality constraints.
    - A_eq (List[List[float]]): Coefficients matrix for equality constraints.
    - b_eq (List[float]): Right-hand side of equality constraints.
    - bounds (List[Tuple[float, float]]): Bounds for decision variables.

    Flow Conservation Constraints:
    - Flow out of the source must equal total flow into other nodes.
    - Flow into the sink must equal total flow out of other nodes.
    - Flow into a node must equal flow out of the same node.

    Capacity Constraints:
    - Capacity constraints for each edge.
    '''
    # Initialize lists to store coefficients and constraints
    c = []  
    A_ub = [] 
    b_ub = [] 
    A_eq = [] 
    b_eq = [] 
    bounds = [] 

    # Define variables for each edge's flow
    for edge in edges:
        # Coefficient for each edge's flow in the objective function
        c.append(0)  
        # Flow should be between 0 and the edge's capacity
        bounds.append((0, edges[edge]))  

    # Flow conservation constraints
    for node in nodes:
        # Flow out of the source must equal total flow into other nodes
        if node == source:  
            A_eq_row = [0] * len(edges)
            for edge in edges:
                if edge[0] == source:
                    A_eq_row[list(edges.keys()).index(edge)] = 1
            A_eq.append(A_eq_row)
            b_eq.append(sum(edges[edge] for edge in edges if edge[0] == source))
        # Flow into the sink must equal total flow out of other nodes
        elif node == sink:  
            A_eq_row = [0] * len(edges)
            for edge in edges:
                if edge[1] == sink:
                    A_eq_row[list(edges.keys()).index(edge)] = 1
            A_eq.append(A_eq_row)
            b_eq.append(sum(edges[edge] for edge in edges if edge[1] == sink))
        else:  
            # Flow into a node must equal flow out of the same node
            A_eq_row = [0] * len(edges)
            A_eq_row_out = [0] * len(edges)
            for edge in edges:
                if edge[0] == node:
                    A_eq_row[list(edges.keys()).index(edge)] = 1
                elif edge[1] == node:
                    A_eq_row_out[list(edges.keys()).index(edge)] = 1
            A_eq.append(A_eq_row_out)
            A_eq.append(A_eq_row)
            b_eq.append(0)
            b_eq.append(0)

    # Add capacity constraints for each edge
    for edge in edges:
        A_ub_row = [0] * len(edges)
        A_ub_row[list(edges.keys()).index(edge)] = 1
        A_ub.append(A_ub_row)
        b_ub.append(edges[edge])

    return c, A_ub, b_ub, A_eq, b_eq, bounds