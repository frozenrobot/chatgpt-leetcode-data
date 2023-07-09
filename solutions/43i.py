class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        # Create a dictionary to store the maximum achievable height for each sum
        dp = {0: 0}

        # Iterate over each rod
        for rod in rods:
            # Create a copy of the dictionary to avoid modifying it while iterating
            curr_dp = dp.copy()

            # Iterate over each sum in the current dictionary
            for total, height in curr_dp.items():
                # Add the rod to one side of the billboard
                sum_with_rod = total + rod
                dp[sum_with_rod] = max(dp.get(sum_with_rod, 0), height)

                # Add the rod to the other side of the billboard
                diff_with_rod = abs(total - rod)
                dp[diff_with_rod] = max(dp.get(diff_with_rod, 0), height + min(total, rod))

        # Return the maximum height achievable for a sum of 0 (balanced billboard)
        return dp[0]
