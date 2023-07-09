class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDepth(self, root):
        if root is None:
            return 0

        # If the current node is a leaf node, return 1
        if root.left is None and root.right is None:
            return 1

        # If the left subtree is empty, recur for the right subtree
        if root.left is None:
            return self.minDepth(root.right) + 1

        # If the right subtree is empty, recur for the left subtree
        if root.right is None:
            return self.minDepth(root.left) + 1

        # If both subtrees are present, take the minimum depth
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        return min(left_depth, right_depth) + 1
