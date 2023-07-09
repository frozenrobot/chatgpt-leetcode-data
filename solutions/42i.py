class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])

        # Create a grid to store the minimum health required
        dp = [[0] * n for _ in range(m)]

        # Fill the grid starting from the bottom-right corner
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    # For the princess's room, the minimum health required is 1
                    dp[i][j] = max(1, 1 - dungeon[i][j])
                elif i == m - 1:
                    # If in the last row, only consider the right cell
                    dp[i][j] = max(dp[i][j + 1] - dungeon[i][j], 1)
                elif j == n - 1:
                    # If in the last column, only consider the bottom cell
                    dp[i][j] = max(dp[i + 1][j] - dungeon[i][j], 1)
                else:
                    # Consider both right and bottom cells, choose the one that requires less health
                    dp[i][j] = max(min(dp[i][j + 1], dp[i + 1][j]) - dungeon[i][j], 1)

        return dp[0][0]
