class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_count = [0] * 26  # List to store the count of each character (assuming lowercase English letters)
        
        # Iterate through the string to count the occurrences of each character
        for char in s:
            char_count[ord(char) - ord('a')] += 1
        
        # Iterate through the string again to find the first non-repeating character
        for i in range(len(s)):
            if char_count[ord(s[i]) - ord('a')] == 1:
                return i
        
        # If no non-repeating character is found, return -1
        return -1
