class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)  # Sort the side lengths in descending order
        
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if a < b + c:  # Check if the side lengths can form a triangle
                return a + b + c
        
        return 0  # Return 0 if no triangle with non-zero area can be formed
