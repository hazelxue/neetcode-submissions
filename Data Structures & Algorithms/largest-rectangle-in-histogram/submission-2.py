class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []# pair:(index, height)
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                popi, poph = stack.pop()
                maxArea = max(maxArea, poph * (i - popi))
                start = popi
            stack.append((start, h))
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea