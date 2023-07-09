class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(board, word, i, j, index):
            # Base case: If all characters in the word have been found
            if index == len(word):
                return True
            
            # Check if the current position is out of bounds or the character doesn't match
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
                return False
            
            # Temporarily mark the current position as visited
            temp = board[i][j]
            board[i][j] = '#'
            
            # Explore the neighboring cells
            found = (dfs(board, word, i-1, j, index+1) or
                     dfs(board, word, i+1, j, index+1) or
                     dfs(board, word, i, j-1, index+1) or
                     dfs(board, word, i, j+1, index+1))
            
            # Restore the original character
            board[i][j] = temp
            
            return found
        
        # Iterate through each cell in the board to find the starting point for the word
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, word, i, j, 0):
                    return True
        
        return False
