class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def dfs(self, start, traversal):
        # Preorder traversal: root, left, right
        if start:
            traversal.append(start.value)
            traversal = self.dfs(start.left, traversal)
            traversal = self.dfs(start.right, traversal)
        return traversal

# Example usage:
#        1
#       / \
#      2   3
#     / \
#    4   5

my_tree = BinaryTree(1)

# Perform DFS
dfs_result = my_tree.dfs(my_tree.root, [])
print("DFS Result:", dfs_result)
