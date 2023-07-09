class Solution(object):
    def isPossibleDivide(self, nums, k):
        if len(nums) % k != 0:
            return False
        
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        
        sorted_nums = sorted(num_count.keys())
        
        for num in sorted_nums:
            if num_count[num] > 0:
                count = num_count[num]
                for i in range(num, num + k):
                    if num_count.get(i, 0) < count:
                        return False
                    num_count[i] -= count
        
        return True
