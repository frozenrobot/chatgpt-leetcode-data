class Solution(object):
    def maxWidthRamp(self, nums):
        n = len(nums)
        max_width = 0
        
        # Create a sorted list of indices based on the element values
        indices = sorted(range(n), key=lambda x: nums[x])
        
        min_index = n
        for i in indices:
            # Update the minimum index encountered so far
            min_index = min(min_index, i)
            
            # Calculate the width ramp using the current index and the minimum index
            width = i - min_index
            
            # Update the maximum width ramp
            max_width = max(max_width, width)
        
        return max_width
