from TreeNode import TreeNode

def is_bst(node, min_value=float('-inf'), max_value=float('inf')):
    """
    Check if a binary tree is a binary search tree (BST).

    Args:
    - node: TreeNode, the root of the current subtree
    - min_value: int, the minimum valid value for nodes in the subtree
    - max_value: int, the maximum valid value for nodes in the subtree

    Returns:
    - bool: True if the subtree rooted at 'node' is a BST, False otherwise
    """
    if not node:
        # Base case: an empty tree is a BST
        return True

    # Check if the current node value is within the valid range
    if not min_value <= node.value <= max_value:
        return False

    # Recursively check left and right subtrees
    return (is_bst(node.left, min_value, node.value - 1) and
            is_bst(node.right, node.value + 1, max_value))

def build_binary_tree():
    """
    Build a binary tree based on user input.

    Returns:
    - TreeNode: The root node of the constructed binary tree.
    """
    print("Enter the elements of the binary tree separated by spaces (use 'None' for missing nodes): ")
    elements = input().split()

    # Stack for maintaining parent nodes
    stack = []

    # Create the root node
    root = TreeNode(int(elements.pop(0)))
    stack.append(root)

    # Iterate through the input elements to build the tree
    while elements:
        current = stack.pop(0)

        left_value = elements.pop(0)
        if left_value != 'None':
            left_node = TreeNode(int(left_value))
            current.left = left_node
            stack.append(left_node)

        if elements:
            right_value = elements.pop(0)
            if right_value != 'None':
                right_node = TreeNode(int(right_value))
                current.right = right_node
                stack.append(right_node)

    return root

# Main program
if __name__ == "__main__":
    # Build the binary tree
    root = build_binary_tree()

    # Check if the binary tree is a BST
    is_bst_result = is_bst(root)

    # Print the result
    if is_bst_result:
        print("The binary tree is a binary search tree (BST).")
    else:
        print("The binary tree is not a binary search tree (BST).")