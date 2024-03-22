from itertools import combinations
import math
from typing import Hashable as Flavour, Hashable as Customer, SupportsInt as Quantity, Union, Iterable, Iterable as Point
from typing import Hashable as Node, SupportsFloat as Cost
import numpy as np
from scipy.optimize import linear_sum_assignment
from typing import Hashable as Flavour, Hashable as Customer, SupportsInt as Quantity, Union

__all__ = ['min_cost_nodes', 'optimal_assignment', 'k_max_clusters']

#------------------------------------------------------------------------------
# [Q1] Solution
#------------------------------------------------------------------------------

def min_cost_nodes(nodes: dict[Node,Cost], edges:set[(Node, Node)]) -> set[Node]: 
    """
    Find the minimum cost nodes that satisfy adjacency constraints.

    Args:
        nodes_costs (dict): A dictionary mapping nodes to their costs.
        edges (set): A set of edges representing adjacency between nodes.

    Returns:
        set: A set of selected nodes that satisfy adjacency constraints.
    """
    # Sort the nodes based on their costs in ascending order
    sorted_nodes = sorted(nodes.items(), key=lambda x: x[1])

    # Initialize a set to store the selected nodes
    selected_nodes = set()
    total_cost = 0.0

    # Iterate through the sorted nodes
    for node, cost in sorted_nodes:
        # Check if adding the current node violates the condition of adjacency
        if all((node, adj_node) not in edges and (adj_node, node) not in edges for adj_node in selected_nodes):
            # If not violated, add the current node to the selected nodes set
            selected_nodes.add(node)
            total_cost += cost

    return selected_nodes, total_cost


#------------------------------------------------------------------------------
# [Q2] Solution
#------------------------------------------------------------------------------

def optimal_assignment(available:dict[Flavour, Quantity], choices:dict[Customer, set[Flavour]]) -> dict[Customer, Union[Flavour, None]]:
    """
    Assign optimal flavours to customers based on their preferences and availability.

    Args:
        available_flavours (dict): A dictionary mapping available flavours to their quantities.
        customer_choices (dict): A dictionary mapping customers to their flavour preferences.

    Returns:
        dict: A dictionary mapping customers to their assigned flavour or None if no flavour can be assigned.
    """
    num_customers = len(choices)
    num_flavours = len(available)

    # Initialize the cost matrix
    cost_matrix = np.zeros((num_customers, num_flavours))

    # Populate the cost matrix
    customer_indices = {customer: index for index, customer in enumerate(choices)}
    flavour_indices = {flavour: index for index, flavour in enumerate(available)}
    for customer, flavour_choices in choices.items():
        for flavour in flavour_choices:
            if flavour in available:
                cost_matrix[customer_indices[customer]][flavour_indices[flavour]] = -1  # Customers prefer lower costs (i.e., more negative values)

    # Use the Hungarian algorithm to find the optimal assignment
    row_indices, col_indices = linear_sum_assignment(cost_matrix)

    # Assign flavours to customers based on the optimal assignment
    assignment = {}
    for customer_idx, flavour_idx in zip(row_indices, col_indices):
        if cost_matrix[customer_idx][flavour_idx] == -1:
            assignment[list(choices.keys())[customer_idx]] = list(available.keys())[flavour_idx]
        else:
            # Assign None if no flavor can be assigned
            assignment[list(choices.keys())[customer_idx]] = None  

    return assignment


#------------------------------------------------------------------------------
# [Q3] Solution
#------------------------------------------------------------------------------

def euclidean_distance(p1: Point, p2: Point) -> float:
    """
    Calculate the Euclidean distance between two points.

    Args:
        p1 (Point): The first point.
        p2 (Point): The second point.

    Returns:
        float: The Euclidean distance between p1 and p2.
    """
    return math.sqrt(sum((x1 - x2) ** 2 for x1, x2 in zip(p1, p2)))

def k_max_clusters(k: int, points: Iterable[Point]) -> list[Iterable[Point]]:
    """
    Cluster points using Kruskal's algorithm to create k maximum clusters.

    Args:
        k (int): The number of clusters to create.
        points (Iterable): Iterable containing points.

    Returns:
        list: A list of k maximum clusters.
    """
    # Calculate the pairwise distances between points
    distances = {(p1, p2): euclidean_distance(p1, p2) for p1, p2 in combinations(points, 2)}
    
    # Sort the distances in increasing order
    sorted_distances = sorted(distances.items(), key=lambda x: x[1])
    
    # Initialize clusters with each point in its own cluster
    clusters = [[point] for point in points]

    # Apply Kruskal's algorithm
    while len(clusters) > k:
        # Get the smallest distance edge
        (p1, p2), distance = sorted_distances.pop(0)

        # Find the clusters containing p1 and p2
        cluster1 = None
        cluster2 = None
        for i, cluster in enumerate(clusters):
            if p1 in cluster:
                cluster1 = i
            if p2 in cluster:
                cluster2 = i
        
        # Merge the clusters
        if cluster1 != cluster2:
            clusters[cluster1].extend(clusters[cluster2])
            del clusters[cluster2]

    return clusters