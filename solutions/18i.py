class Solution(object):
    def findLucky(self, arr):
        frequency = {}
        
        # Count the frequency of each number in the array
        for num in arr:
            frequency[num] = frequency.get(num, 0) + 1
        
        lucky_numbers = []
        
        # Find the lucky numbers
        for num, freq in frequency.items():
            if num == freq:
                lucky_numbers.append(num)
        
        if not lucky_numbers:
            return -1
        
        return max(lucky_numbers)
