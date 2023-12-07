from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def bfs(self):
        result = []
        if self.root is None:
            return result

        queue = deque([self.root])

        while queue:
            current_node = queue.popleft()
            result.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return result

# Example usage:
#        1
#       / \
#      2   3
#     / \
#    4   5

my_tree = BinaryTree(1)

# Perform BFS
bfs_result = my_tree.bfs()
print("BFS Result:", bfs_result)
