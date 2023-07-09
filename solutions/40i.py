import heapq

class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        # Build the adjacency list representation of the graph
        graph = [[] for _ in range(n)]
        for i, (a, b) in enumerate(edges):
            p = succProb[i]
            graph[a].append((b, p))
            graph[b].append((a, p))

        # Initialize distances with negative logarithm of success probabilities
        distances = [-float('inf')] * n
        distances[start] = 0.0

        # Priority queue for Dijkstra's algorithm
        pq = []
        heapq.heappush(pq, (-distances[start], start))

        # Dijkstra's algorithm
        while pq:
            dist, node = heapq.heappop(pq)
            dist = -dist  # Retrieve the distance value

            # Skip if the node has been visited before with a shorter distance
            if dist > distances[node]:
                continue

            # Explore the neighbors of the current node
            for neighbor, prob in graph[node]:
                new_dist = dist + math.log(prob)  # Calculate the new distance
                if new_dist > distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (-new_dist, neighbor))

        # Return the success probability at the end node
        return math.exp(distances[end])
