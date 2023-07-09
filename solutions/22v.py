class Solution(object):
    def maxWidthRamp(self, nums):
        n = len(nums)
        indices = list(range(n))
        
        # Sort indices based on nums using a modified merge sort
        indices.sort(key=lambda x: nums[x])
        
        max_width = 0
        min_index = n
        
        # Iterate through the sorted indices and update max_width
        for index in indices:
            max_width = max(max_width, index - min_index)
            min_index = min(min_index, index)
        
        return max_width
