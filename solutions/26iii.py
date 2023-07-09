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
        
        dp = [[] for _ in range(n + 1)]
        dp[0].append(None)
        
        for length in range(1, n + 1):
            for root_val in range(1, length + 1):
                left_length = root_val - 1
                right_length = length - root_val
                
                for left_tree in dp[left_length]:
                    for right_tree in dp[right_length]:
                        root = TreeNode(root_val)
                        root.left = self.clone_tree(left_tree, 0)
                        root.right = self.clone_tree(right_tree, root_val)
                        dp[length].append(root)
        
        return dp[n]
    
    def clone_tree(self, node, offset):
        if node is None:
            return None
        
        new_node = TreeNode(node.val + offset)
        new_node.left = self.clone_tree(node.left, offset)
        new_node.right = self.clone_tree(node.right, offset)
        
        return new_node
