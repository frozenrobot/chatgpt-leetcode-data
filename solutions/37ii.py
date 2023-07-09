from collections import deque

class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(isWater), len(isWater[0])
        height = [[-1] * n for _ in range(m)]  # Initialize the height matrix

        queue = deque()  # Queue for bidirectional BFS traversal

        # Initialize the water cells with height 0 and add them to the queue
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    queue.append((i, j, 1))  # Mark water cells with source = 1

        # Perform bidirectional BFS traversal starting from the water cells and land cells simultaneously
        while queue:
            x, y, source = queue.popleft()

            # Check adjacent cells (up, down, left, right)
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy

                # Check if the adjacent cell is within the grid and not visited
                if 0 <= nx < m and 0 <= ny < n and height[nx][ny] == -1:
                    height[nx][ny] = height[x][y] + 1
                    queue.append((nx, ny, source))

        return height
