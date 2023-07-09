class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])

        # Create a one-dimensional array to store the minimum health required for the current row
        dp = [0] * n

        # Fill the array starting from the last column
        dp[n - 1] = max(1, 1 - dungeon[m - 1][n - 1])

        # Calculate the minimum health required for each cell in the grid
        for j in range(n - 2, -1, -1):
            dp[j] = max(dp[j + 1] - dungeon[m - 1][j], 1)

        # Update the array for each row, starting from the second last row
        for i in range(m - 2, -1, -1):
            # Update the last column of the current row
            dp[n - 1] = max(dp[n - 1] - dungeon[i][n - 1], 1)
            
            # Update the rest of the cells in the current row
            for j in range(n - 2, -1, -1):
                dp[j] = max(min(dp[j], dp[j + 1]) - dungeon[i][j], 1)

        return dp[0]
