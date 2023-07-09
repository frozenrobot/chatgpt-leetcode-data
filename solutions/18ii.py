from collections import Counter

class Solution(object):
    def findLucky(self, arr):
        frequency = Counter(arr)
        max_lucky = -1
        
        for num, freq in frequency.items():
            if num == freq:
                max_lucky = max(max_lucky, num)
        
        return max_lucky
