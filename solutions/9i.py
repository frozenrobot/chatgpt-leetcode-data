class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_dict = {}
        t_dict = {}
        
        # Count the frequency of each character in string s
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
        
        # Count the frequency of each character in string t
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        
        # Compare the frequencies of characters in s and t
        for char in t_dict:
            if char not in s_dict or t_dict[char] > s_dict[char]:
                return char
