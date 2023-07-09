from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDepth(self, root):
        if root is None:
            return 0

        # Create a queue for BFS
        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            # Check if the current node is a leaf node
            if node.left is None and node.right is None:
                return depth

            # Add the left and right children to the queue
            if node.left is not None:
                queue.append((node.left, depth + 1))
            if node.right is not None:
                queue.append((node.right, depth + 1))
