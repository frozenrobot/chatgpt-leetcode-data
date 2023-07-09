import heapq

class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(isWater), len(isWater[0])
        height = [[-1] * n for _ in range(m)]  # Initialize the height matrix

        # Initialize the priority queue with water cells
        pq = []
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    heapq.heappush(pq, (0, i, j))  # Priority queue based on height

        # Perform Dijkstra's algorithm
        while pq:
            h, x, y = heapq.heappop(pq)

            # Check adjacent cells (up, down, left, right)
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy

                # Check if the adjacent cell is within the grid and not visited
                if 0 <= nx < m and 0 <= ny < n and height[nx][ny] == -1:
                    height[nx][ny] = h + 1
                    heapq.heappush(pq, (h + 1, nx, ny))  # Add the adjacent cell to the priority queue

        return height
