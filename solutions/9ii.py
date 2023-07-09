class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        xor_value = 0
        
        # XOR all the characters in string s and t
        for char in s + t:
            xor_value ^= ord(char)
        
        # The remaining XOR value will be the ASCII value of the added letter
        return chr(xor_value)
