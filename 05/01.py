from TreeNode import TreeNode

class BinarySearchTree:
    def __init__(self):
        """
        Initialize an empty binary search tree.
        """
        self.root = None

    # Function to insert a value into the BST.
    def insert(self, value):
        """
        Insert a value into the binary search tree.
        """
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    # Function to recursively insert a value into the BST.
    def _insert_recursively(self, node, value):
        """
        Recursively insert a value into the binary search tree.
        """
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)

    # Function to perform inorder traversal of the BST.
    def inorder_traversal(self, node, result):
        """
        Perform an inorder traversal of the binary search tree.
        """
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)

    # Function to perform kth smallest element of the BST.
    def kth_smallest(self, k):
        """
        Find the kth smallest element in the binary search tree.
        """
        result = []
        self.inorder_traversal(self.root, result)
        if 0 < k <= len(result):
            return result[k - 1]
        else:
            return None
    
    # Function to perform kth smallest element of the BST.
    def kth_largest(self, k):
        """
        Find the kth largest element in the binary search tree.
        """
        result = []
        self.inorder_traversal(self.root, result)
        if 0 < k <= len(result):
            return result[-k]
        else:
            return None



# Main program
if __name__ == "__main__":
    bst = BinarySearchTree()

    # Inserting elements
    nums = input("Enter the elements of the binary search tree separated by spaces: ").split()
    for num in nums:
        bst.insert(int(num))

    k = int(input("Enter the value of k: "))

    # Inorder Traversal
    inorder = []
    bst.inorder_traversal(bst.root, inorder)
    print(inorder)

    # Finding kth smallest and kth largest elements
    kth_smallest = bst.kth_smallest(k)
    kth_largest = bst.kth_largest(k)

    print(f"{k}th smallest element: {kth_smallest}")
    print(f"{k}th largest element: {kth_largest}")