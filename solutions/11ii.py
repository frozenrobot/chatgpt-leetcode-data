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
        if not root:
            return []
        
        result = []
        stack = [root]  # Use a stack to keep track of nodes
        
        while stack:
            node = stack.pop()  # Pop the top node from the stack
            result.append(node.val)  # Visit the current node
            
            # Push the right child first and then the left child to the stack
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result
