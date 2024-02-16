from TreeNode import TreeNode

def find_lca(root, node1, node2):
    """
    Find the lowest common ancestor (LCA) of two nodes in a binary search tree (BST).

    Args:
    - root: TreeNode, the root of the BST
    - node1: int, value of the first node
    - node2: int, value of the second node

    Returns:
    - TreeNode or None: The lowest common ancestor node, or None if not found.
    """
    if not root:
        return None

    if root.value > node1 and root.value > node2:
        # Both nodes are in the left subtree
        return find_lca(root.left, node1, node2)
    elif root.value < node1 and root.value < node2:
        # Both nodes are in the right subtree
        return find_lca(root.right, node1, node2)
    else:
        # Current node is the LCA
        return root

def build_binary_search_tree():
    """
    Build a binary search tree based on user input.

    Returns:
    - TreeNode: The root node of the constructed binary search tree.
    """
    print("Enter the elements of the binary search tree separated by spaces: ")
    elements = list(map(int, input().split()))

    root = TreeNode(elements.pop(0))
    for element in elements:
        insert_node(root, element)

    return root

def insert_node(root, value):
    """
    Insert a node with the given value into the binary search tree.

    Args:
    - root: TreeNode, the root of the binary search tree
    - value: int, the value to be inserted
    """
    if not root:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_node(root.left, value)
    elif value > root.value:
        root.right = insert_node(root.right, value)
    return root

# Main program
if __name__ == "__main__":
    # Build the binary search tree
    root = build_binary_search_tree()

    # Get nodes for which LCA needs to be found
    node1 = int(input("Enter the value of the first node: "))
    node2 = int(input("Enter the value of the second node: "))

    # Find the lowest common ancestor
    lca = find_lca(root, node1, node2)

    # Print the result
    if lca:
        print(f"The lowest common ancestor of {node1} and {node2} is: {lca.value}")
    else:
        print("No common ancestor found.")