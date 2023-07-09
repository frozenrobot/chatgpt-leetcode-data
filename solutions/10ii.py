from collections import OrderedDict

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_count = OrderedDict()  # Ordered dictionary to maintain the order of insertion
        
        # Iterate through the string
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Iterate through the ordered dictionary to find the first non-repeating character
        for char, count in char_count.items():
            if count == 1:
                return s.index(char)
        
        # If no non-repeating character is found, return -1
        return -1
