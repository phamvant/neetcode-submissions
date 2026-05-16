class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        ret = 0

        while r > l:
            ret = max(ret, (max(heights[l], heights[r]) - abs(max(heights[l], heights[r]) - min(heights[l], heights[r]))) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return ret