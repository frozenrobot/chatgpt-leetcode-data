class Solution(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        if self.countIslands(grid) != 1:
            return 0
        
        island_cells = self.getIslandCells(grid, m, n)
        if self.canDisconnect(island_cells, grid, m, n):
            return 1
        
        return 2
    
    def countIslands(self, grid):
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    count += 1
                    self.dfs(grid, i, j, visited)
        return count
    
    def dfs(self, grid, i, j, visited):
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited[i][j] = True
        for dx, dy in directions:
            nx, ny = i + dx, j + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and not visited[nx][ny]:
                self.dfs(grid, nx, ny, visited)
    
    def getIslandCells(self, grid, m, n):
        island_cells = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    island_cells.add((i, j))
        return island_cells
    
    def canDisconnect(self, island_cells, grid, m, n):
        for cell in island_cells:
            i, j = cell
            grid[i][j] = 0
            if self.countIslands(grid) != 1:
                grid[i][j] = 1
                return True
            grid[i][j] = 1
        return False
