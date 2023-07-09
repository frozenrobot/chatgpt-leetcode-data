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
        eof = False  # Flag to indicate end of file
        buf4_idx = 0  # Index for the buffer of characters read from read4
        buf4_chars = 0  # Number of characters read from read4
        
        while total_chars < n and (not eof or buf4_idx < buf4_chars):
            if buf4_idx == buf4_chars:
                # Only read from read4 when all characters in the buffer have been processed
                buf4_chars = read4(buf4)
                buf4_idx = 0
                if buf4_chars == 0:
                    # If no more characters to read, set the end of file flag
                    eof = True
            
            # Copy the characters from buf4 to buf
            while total_chars < n and buf4_idx < buf4_chars:
                buf[total_chars] = buf4[buf4_idx]
                total_chars += 1
                buf4_idx += 1
        
        return total_chars
