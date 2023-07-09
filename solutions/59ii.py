class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        def make_special(s):
            if s == "":
                return ""

            count = 0
            substrings = []
            start = 0
            result = ""

            for i, char in enumerate(s):
                if char == "1":
                    count += 1
                else:
                    count -= 1

                if count == 0:
                    substr = "1" + make_special(s[start+1:i]) + "0"
                    substrings.append(substr)
                    start = i + 1

            substrings.sort(reverse=True)
            return result.join(substrings)

        return make_special(s)
