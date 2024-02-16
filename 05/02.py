from TreeNode import AVLTreeNode as TreeNode

class AVLTree:
    def __init__(self):
        """
        Initialize an empty AVL tree.
        """
        self.root = None

    def insert(self, value):
        """
        Insert a value into the AVL tree.
        """
        self.root = self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        """
        Recursively insert a value into the AVL tree and perform necessary rotations to maintain balance.
        """
        if not node:
            return TreeNode(value)
        elif value < node.value:
            node.left = self._insert_recursively(node.left, value)
        else:
            node.right = self._insert_recursively(node.right, value)

        # Update height of current node
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance_factor = self._get_balance(node)

        # Perform rotations if necessary to maintain AVL property
        if balance_factor > 1 and value < node.left.value:
            return self._right_rotate(node)
        if balance_factor < -1 and value > node.right.value:
            return self._left_rotate(node)
        if balance_factor > 1 and value > node.left.value:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance_factor < -1 and value < node.right.value:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _get_height(self, node):
        """
        Get the height of a node.
        """
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        """
        Get the balance factor of a node.
        """
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _left_rotate(self, z):
        """
        Perform a left rotation at the given node.
        """
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _right_rotate(self, z):
        """
        Perform a right rotation at the given node.
        """
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def inorder_traversal(self, node, result):
        """
        Perform an inorder traversal of the AVL tree.
        """
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)

# Function to convert a binary tree into an AVL tree
def binary_tree_to_avl(root):
    """
    Convert a binary tree into an AVL tree using rotations.
    """
    if not root:
        return AVLTree()

    avl_tree = AVLTree()
    nodes = [root]

    while nodes:
        node = nodes.pop(0)
        avl_tree.insert(node.value)

        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)

    return avl_tree

# Function to build a binary tree from given input values
def build_binary_tree():
    """
    Build a binary tree based on user input.
    """
    root_value = int(input("Enter the value of root node: "))
    root = TreeNode(root_value)

    queue = [root]
    while queue:
        current = queue.pop(0)
        left_value = input(f"Enter the left child value of {current.value} (or type 'None' if no left child): ")
        if left_value != 'None':
            left_node = TreeNode(int(left_value))
            current.left = left_node
            queue.append(left_node)

        right_value = input(f"Enter the right child value of {current.value} (or type 'None' if no right child): ")
        if right_value != 'None':
            right_node = TreeNode(int(right_value))
            current.right = right_node
            queue.append(right_node)

    return root

# Main program
if __name__ == "__main__":
    root = build_binary_tree()
    avl_tree = binary_tree_to_avl(root)

    result = []
    avl_tree.inorder_traversal(avl_tree.root, result)
    print("Inorder traversal of AVL tree:")
    print(result)