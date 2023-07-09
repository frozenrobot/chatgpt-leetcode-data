class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        def make_special(s):
            substrings = []
            count = i = 0
            result = ""

            for j, char in enumerate(s):
                count = count + 1 if char == "1" else count - 1

                if count == 0:
                    substr = "1" + make_special(s[i+1:j]) + "0"
                    substrings.append(substr)
                    i = j + 1

            substrings.sort(reverse=True)
            return "".join(substrings)

        return make_special(s)
