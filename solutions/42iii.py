class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])

        # Calculate the minimum health required for the princess's room
        dungeon[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])

        # Calculate the minimum health required for the last row
        for j in range(n - 2, -1, -1):
            dungeon[m - 1][j] = max(dungeon[m - 1][j + 1] - dungeon[m - 1][j], 1)

        # Calculate the minimum health required for the last column and the rest of the cells
        for i in range(m - 2, -1, -1):
            dungeon[i][n - 1] = max(dungeon[i + 1][n - 1] - dungeon[i][n - 1], 1)
            for j in range(n - 2, -1, -1):
                dungeon[i][j] = max(min(dungeon[i][j + 1], dungeon[i + 1][j]) - dungeon[i][j], 1)

        return dungeon[0][0]
