class Solution(object):
    def findLucky(self, arr):
        max_lucky = -1
        
        # Count the frequency of each number in the array
        for num in set(arr):
            freq = arr.count(num)
            if num == freq:
                max_lucky = max(max_lucky, num)
        
        return max_lucky
