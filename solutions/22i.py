class Solution(object):
    def maxWidthRamp(self, nums):
        stack = []
        n = len(nums)
        
        # Find the indices of elements in decreasing order of their values
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        # Find the maximum width ramp
        max_width = 0
        for j in range(n - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                max_width = max(max_width, j - stack.pop())
            
        return max_width
