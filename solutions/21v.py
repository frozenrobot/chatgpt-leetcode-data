class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def backtrack(board, word, i, j, index, memo):
            # Base case: If all characters in the word have been found
            if index == len(word):
                return True
            
            # Check if the current position is out of bounds or the character doesn't match
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
                return False
            
            # Check if the solution for the current position has already been computed
            if memo[i][j]:
                return False
            
            # Temporarily mark the current position as visited
            temp = board[i][j]
            board[i][j] = '#'
            
            # Explore the neighboring cells
            found = (backtrack(board, word, i-1, j, index+1, memo) or
                     backtrack(board, word, i+1, j, index+1, memo) or
                     backtrack(board, word, i, j-1, index+1, memo) or
                     backtrack(board, word, i, j+1, index+1, memo))
            
            # Restore the original character
            board[i][j] = temp
            
            # Memoize the result for the current position
            memo[i][j] = found
            
            return found
        
        # Create a memoization grid to store computed results
        memo = [[False] * len(board[0]) for _ in range(len(board))]
        
        # Iterate through each cell in the board to find the starting point for the word
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(board, word, i, j, 0, memo):
                    return True
        
        return False
