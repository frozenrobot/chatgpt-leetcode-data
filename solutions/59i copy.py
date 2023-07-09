class Solution(object):
    def __init__(self):
        self.rec_layer = 0

    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        def make_special(s):
            self.rec_layer += 1
            if s == "":
                self.rec_layer -= 1
                return ""

            count = 0
            substrings = []
            start = 0

            for i, char in enumerate(s):
                if char == "1":
                    count += 1
                else:
                    count -= 1

                if count == 0:
                    print(f"rec_layer: {self.rec_layer}, count: {count}, start: {start}, s[start+1:i]: '{s[start+1:i]}'")
                    substrings.append("1" + make_special(s[start+1:i]) + "0")
                    start = i + 1

            substrings.sort(reverse=True)
            self.rec_layer -= 1
            return "".join(substrings)

        return make_special(s)

Solution().makeLargestSpecial("1111000011110000")