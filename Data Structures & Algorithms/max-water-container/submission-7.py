class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        ret = 0

        while l < r:
            # The width is (r - l), and the limiting height is the smaller of the two
            current_area = min(heights[l], heights[r]) * (r - l)
            if current_area > ret:
                ret = current_area
            
            # Move the pointer pointing to the shorter line inward
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return ret