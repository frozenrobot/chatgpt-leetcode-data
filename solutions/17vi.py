class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        result = ""
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            digit_sum = carry
            if i >= 0:
                digit_sum += int(a[i])
                i -= 1
            if j >= 0:
                digit_sum += int(b[j])
                j -= 1
            result = str(digit_sum % 2) + result
            carry = digit_sum // 2
        
        return result
