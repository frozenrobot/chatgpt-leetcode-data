# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        
        def generate_trees(start, end, memo):
            if start > end:
                return [None]
            
            if (start, end) in memo:
                return memo[(start, end)]
            
            all_trees = []
            for i in range(start, end+1):
                left_trees = generate_trees(start, i-1, memo)
                right_trees = generate_trees(i+1, end, memo)
                
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
            
            memo[(start, end)] = all_trees
            return all_trees
        
        memo = {}
        return generate_trees(1, n, memo)
