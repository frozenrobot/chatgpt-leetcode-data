class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        deletions = 0  # Minimum number of deletions needed
        count_b = 0  # Count of 'b' characters encountered

        for char in s:
            if char == 'a':
                # If 'a' is encountered, we need to check if there are any preceding 'b' characters
                # If yes, we can delete the 'a' to balance the string
                deletions = min(deletions + 1, count_b)
            else:
                # If 'b' is encountered, increment the count of 'b' characters
                count_b += 1

        return deletions
