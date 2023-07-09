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
        curr = root
        
        while curr:
            if not curr.left:
                result.append(curr.val)
                curr = curr.right
            else:
                predecessor = curr.left
                
                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right
                
                if not predecessor.right:
                    result.append(curr.val)
                    predecessor.right = curr
                    curr = curr.left
                else:
                    predecessor.right = None
                    curr = curr.right
        
        return result
