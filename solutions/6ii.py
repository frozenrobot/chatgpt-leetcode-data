class Solution(object):
    def longestPalindrome(self, s):
        char_count = [0] * 52
        for char in s:
            if 'a' <= char <= 'z':
                index = ord(char) - ord('a')
            else:
                index = ord(char) - ord('A') + 26
            char_count[index] += 1

        longest_length = 0
        odd_count = 0
        for count in char_count:
            if count % 2 == 0:
                longest_length += count
            else:
                longest_length += count - 1
                odd_count = 1

        return longest_length + odd_count
