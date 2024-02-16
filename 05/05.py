from TreeNode import TreeNode

def build_bst_from_sorted_array(sorted_array):
    """
    Build a binary search tree from a sorted array.

    Args:
    - sorted_array: list, a sorted array of elements

    Returns:
    - TreeNode: The root node of the constructed binary search tree.
    """
    if not sorted_array:
        return None

    mid_index = len(sorted_array) // 2
    root = TreeNode(sorted_array[mid_index])

    root.left = build_bst_from_sorted_array(sorted_array[:mid_index])
    root.right = build_bst_from_sorted_array(sorted_array[mid_index + 1:])

    return root

def inorder_traversal(node):
    """
    Perform an inorder traversal of the binary search tree.

    Args:
    - node: TreeNode, the root of the binary search tree
    """
    if node:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)

# Main program
if __name__ == "__main__":
    # Input sorted array from user
    print("Enter the elements of the sorted array separated by spaces:")
    sorted_array = list(map(int, input().split()))

    # Build the binary search tree
    root = build_bst_from_sorted_array(sorted_array)

    # Perform inorder traversal to demonstrate the construction
    print("Inorder traversal of the constructed binary search tree:")
    inorder_traversal(root)