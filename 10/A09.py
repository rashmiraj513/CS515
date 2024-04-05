import pulp

__all__ = ['color_bt', 'color_lp']

#------------------------------------------------------------------------------
# [Q1] Solution
#------------------------------------------------------------------------------
def is_safe(adjm, vertex, c, color):
    '''
    Check if it's safe to assign color 'c' to the vertex 'vertex' based on its neighbors' colors.

    Parameters:
    - adjm (list[list[bool]]): Adjacency matrix representing the graph.
    - vertex (int): Current vertex being considered.
    - c (int): Color being checked.
    - color (list[int]): List of colors assigned to vertices so far.

    Returns:
    - bool: True if it's safe to assign the color 'c' to 'vertex', False otherwise.
    '''
    for i in range(len(adjm)):
        if adjm[vertex][i] and color[i] == c:
            return False
    return True

def color_graph(adjm, vertex, color):
    '''
    Recursively try to color each vertex using backtracking.

    Parameters:
    - adjm (list[list[bool]]): Adjacency matrix representing the graph.
    - vertex (int): Current vertex being considered.
    - color (list[int]): List of colors assigned to vertices so far.

    Returns:
    - bool: True if a valid coloring is found, False otherwise.
    '''
    if vertex == len(adjm):
        return True
    
    for c in range(3):
        if is_safe(adjm, vertex, c, color):
            color[vertex] = c
            if color_graph(adjm, vertex + 1, color):
                return True
            color[vertex] = -1
    
    return False

def color_bt(adjm:list[list[bool]]) -> list[int]:
    '''
    Color the graph represented by the adjacency matrix using backtracking with 3 colors.

    Parameters:
    - adjm (list[list[bool]]): Adjacency matrix representing the graph.

    Returns:
    - list[int]: List of colors assigned to vertices if a valid coloring is found,
                 empty list if not possible to color with 3 colors.
    '''
    n = len(adjm)
    color = [-1] * n
    
    if not color_graph(adjm, 0, color):
        return []
    
    return color

#------------------------------------------------------------------------------
# [Q2] Solution
#------------------------------------------------------------------------------

def color_lp(adjm:list[list[bool]]):
    '''
    Find the chromatic number of the graph using integer linear programming with PuLP.

    Parameters:
    - adjm (list[list[bool]]): Adjacency matrix representing the graph.

    Returns:
    - int: Chromatic number of the graph.
    '''
    num_vertices = len(adjm)

    # Create an LP model
    model = pulp.LpProblem("Graph_Coloring", pulp.LpMinimize)

    # Decision variables: x_ik
    x = [[pulp.LpVariable(f"x_{i}_{k}", cat=pulp.LpBinary) 
          for k in range(num_vertices)] for i in range(num_vertices)]

    # Auxiliary variables: y_k
    y = [pulp.LpVariable(f"y_{k}", cat=pulp.LpBinary) for k in range(num_vertices)]

    # Objective function
    model += pulp.lpSum(y)

    # Constraints
    for i in range(num_vertices):
        model += pulp.lpSum(x[i]) == 1  
        for j in range(i + 1, num_vertices):
            if adjm[i][j]:
                for k in range(num_vertices):
                    model += x[i][k] + x[j][k] <= 1  

    for i in range(num_vertices):
        for k in range(num_vertices):
            model += x[i][k] <= y[k]

    # Solve the LP model
    status = model.solve(pulp.PULP_CBC_CMD(msg=False))  

    return pulp.value(model.objective)