# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.preorderTraversalRecursive(root, result)
        return result
    
    def preorderTraversalRecursive(self, node, result):
        if node is None:
            return
        
        result.append(node.val)  # Visit the current node
        self.preorderTraversalRecursive(node.left, result)  # Traverse left subtree
        self.preorderTraversalRecursive(node.right, result)  # Traverse right subtree
