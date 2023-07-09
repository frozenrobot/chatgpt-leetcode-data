class Solution(object):
    def countPaths(self, grid):
        MOD = int(1e9) + 7
        m, n = len(grid), len(grid[0])

        dp = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]

            count = 1
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > grid[i][j]:
                    count = (count + dfs(ni, nj)) % MOD

            dp[i][j] = count
            return count

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = (ans + dfs(i, j)) % MOD

        return ans
