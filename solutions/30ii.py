class Solution(object):
    def findBuildings(self, heights):
        res = []
        max_height = 0

        # Traverse the buildings from right to left
        for i in range(len(heights)-1, -1, -1):
            # Check if the current building has an ocean view
            if heights[i] > max_height:
                res.append(i)
                max_height = heights[i]

        # Return the result in increasing order
        return res[::-1]
