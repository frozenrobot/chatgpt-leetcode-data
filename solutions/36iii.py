from collections import Counter

class Solution(object):
    def isPossibleDivide(self, nums, k):
        if len(nums) % k != 0:
            return False
        
        num_count = Counter(nums)
        
        while num_count:
            min_num = min(num_count.keys())
            count = num_count[min_num]
            
            for num in range(min_num, min_num + k):
                if num_count[num] < count:
                    return False
                num_count[num] -= count
                if num_count[num] == 0:
                    del num_count[num]
        
        return True
