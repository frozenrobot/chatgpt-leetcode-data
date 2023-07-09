class Solution(object):
    def maxWidthRamp(self, nums):
        stack = []
        n = len(nums)
        
        # Build the stack in decreasing order of nums elements
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        max_width = 0
        
        # Iterate from right to left to find the maximum width ramp
        for j in range(n - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                max_width = max(max_width, j - stack.pop())
        
        return max_width
