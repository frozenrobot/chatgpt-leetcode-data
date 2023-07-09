class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        result = []
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            num1 = int(a[i]) if i >= 0 else 0
            num2 = int(b[j]) if j >= 0 else 0
            current_sum = num1 + num2 + carry
            result.append(str(current_sum % 2))
            carry = current_sum // 2
            i -= 1
            j -= 1
        
        return ''.join(result[::-1])
