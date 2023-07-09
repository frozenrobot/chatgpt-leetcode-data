class Solution(object):
    def findBuildings(self, heights):
        ocean_view_buildings = []
        max_height = 0

        # Traverse the buildings from right to left
        for i in range(len(heights)-1, -1, -1):
            # Check if the current building has an ocean view
            if heights[i] > max_height:
                ocean_view_buildings.append(i)
                max_height = heights[i]

        # Reverse the order of the ocean view buildings to obtain the increasing order
        return ocean_view_buildings[::-1]
