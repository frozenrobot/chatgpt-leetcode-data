class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Create a dictionary to store the count of each character in the string
        char_count = {}
        
        # Iterate through the string to count the occurrences of each character
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Iterate through the string again to find the first non-repeating character
        for i in range(len(s)):
            if char_count[s[i]] == 1:
                return i
        
        # If no non-repeating character is found, return -1
        return -1
