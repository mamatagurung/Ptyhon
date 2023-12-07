class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

# Example usage:
#        1
#       / \
#      2   3
#     / \
#    4   5

my_tree = BinaryTree(1)
my_tree.root.left = TreeNode(2)
my_tree.root.right = TreeNode(3)
my_tree.root.left.left = TreeNode(4)
my_tree.root.left.right = TreeNode(5)
