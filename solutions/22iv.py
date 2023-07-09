class Solution(object):
    def maxWidthRamp(self, nums):
        n = len(nums)
        
        # Create a list of tuples (value, index) for each element in nums
        nums_with_indices = [(nums[i], i) for i in range(n)]
        
        # Sort nums_with_indices in ascending order of values
        nums_with_indices.sort()
        
        max_width = 0
        min_index = n
        
        # Iterate through nums_with_indices and update max_width
        for _, index in nums_with_indices:
            max_width = max(max_width, index - min_index)
            min_index = min(min_index, index)
        
        return max_width
