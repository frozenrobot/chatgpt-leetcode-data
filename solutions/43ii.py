class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        # Calculate the maximum possible sum
        max_sum = sum(rods)

        # Create a 2D list to store the maximum achievable height for each sum
        # dp[i][j] represents the maximum height achievable with a difference of j for the first i rods
        dp = [[-float('inf')] * (2 * max_sum + 1) for _ in range(len(rods) + 1)]
        dp[0][max_sum] = 0

        # Iterate over each rod
        for i in range(1, len(rods) + 1):
            rod = rods[i - 1]

            # Iterate over each possible difference
            for j in range(-max_sum, max_sum + 1):
                # Skip if the current difference is not achievable
                if dp[i - 1][j + max_sum] == -float('inf'):
                    continue

                # Update the maximum heights for the next rod
                dp[i][j + rod + max_sum] = max(dp[i][j + rod + max_sum], dp[i - 1][j + max_sum] + rod)
                dp[i][j - rod + max_sum] = max(dp[i][j - rod + max_sum], dp[i - 1][j + max_sum])

                # Keep the current rod
                dp[i][j + max_sum] = max(dp[i][j + max_sum], dp[i - 1][j + max_sum])

        # Return the maximum height achievable for a sum of 0 (balanced billboard)
        return dp[len(rods)][max_sum]
