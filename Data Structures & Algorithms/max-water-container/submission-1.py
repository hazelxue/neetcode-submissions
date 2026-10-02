class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0

        l, r = 0, len(heights) - 1
        left_max = heights[l]
        right_max = heights[r]
        
        while l < r:
            h = min(left_max, right_max)
            water = (r - l) * h
            max_water = max(max_water, water)
            if left_max < right_max:
                l += 1
                left_max = max(left_max, heights[l])
            else:
                r -= 1
                right_max = max(right_max, heights[r])
        return max_water
