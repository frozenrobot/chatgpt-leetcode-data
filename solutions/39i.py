class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        # Sort the numbers in ascending order
        nums.sort()

        # Initialize variables to store the maximum subset and its length
        max_subset = []
        max_length = 0

        # Initialize two lists: dp to track the length of subsets and prev to track the previous element in the subset
        dp = [1] * len(nums)
        prev = [-1] * len(nums)

        # Iterate through the numbers
        for i in range(len(nums)):
            # Iterate from the beginning of the list up to the current number
            for j in range(i):
                # If nums[i] is divisible by nums[j], it can be part of a larger subset
                if nums[i] % nums[j] == 0:
                    # Update the length of the subset and the previous element
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j

            # Check if the current subset is the largest
            if dp[i] > max_length:
                max_length = dp[i]
                max_subset = []

                # Reconstruct the subset using the previous elements
                k = i
                while k != -1:
                    max_subset.append(nums[k])
                    k = prev[k]

        # Return the largest subset
        return max_subset[::-1]
