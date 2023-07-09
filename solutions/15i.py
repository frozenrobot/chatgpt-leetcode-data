class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        # Create a buffer with enough space to store characters
        buf4 = [''] * 4
        total_chars = 0  # Counter for total characters read
        
        while total_chars < n:
            # Read up to 4 characters from the file
            chars_read = read4(buf4)
            
            # If no more characters to read, break the loop
            if chars_read == 0:
                break
            
            # Copy the characters from buf4 to buf
            for i in range(min(chars_read, n - total_chars)):
                buf[total_chars] = buf4[i]
                total_chars += 1
        
        return total_chars
