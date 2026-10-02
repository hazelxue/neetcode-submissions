class Solution:
    def trap(self, height: List[int]) -> int:
        rain = 0
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]

        while l <= r:
            if left_max < right_max:
                left_max = max(left_max, height[l])
                rain += max(0, left_max - height[l])
                l += 1
            else:
                right_max = max(right_max, height[r])
                rain += max(0, right_max - height[r])
                r -= 1
        return rain