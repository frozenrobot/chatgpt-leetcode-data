from collections import Counter
import heapq

class Solution(object):
    def isPossibleDivide(self, nums, k):
        if len(nums) % k != 0:
            return False
        
        num_count = Counter(nums)
        min_heap = []
        
        for num in num_count:
            heapq.heappush(min_heap, num)
        
        while min_heap:
            curr = heapq.heappop(min_heap)
            
            if num_count[curr] == 0:
                continue
            
            count = num_count[curr]
            
            for i in range(curr, curr + k):
                if num_count[i] < count:
                    return False
                num_count[i] -= count
        
        return True
