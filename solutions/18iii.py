class Solution(object):
    def findLucky(self, arr):
        frequency = [0] * 501  # Initialize frequency array
        
        # Count the frequency of each number in the array
        for num in arr:
            frequency[num] += 1
        
        max_lucky = -1
        
        # Find the maximum lucky number
        for num in range(1, len(frequency)):
            if num == frequency[num]:
                max_lucky = num
        
        return max_lucky
