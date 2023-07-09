class Solution(object):
    def longestPalindrome(self, s):
        char_count = [0] * 52
        odd_count = 0

        for char in s:
            if 'a' <= char <= 'z':
                index = ord(char) - ord('a')
            else:
                index = ord(char) - ord('A') + 26
            char_count[index] += 1

            if char_count[index] % 2 == 0:
                odd_count -= 1
            else:
                odd_count += 1

        longest_length = len(s) - odd_count
        if odd_count > 0:
            longest_length += 1

        return longest_length
