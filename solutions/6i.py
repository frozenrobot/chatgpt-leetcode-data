class Solution(object):
    def longestPalindrome(self, s):
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        longest_length = 0
        odd_count = 0
        for count in char_count.values():
            if count % 2 == 0:
                longest_length += count
            else:
                longest_length += count - 1
                odd_count = 1

        return longest_length + odd_count
