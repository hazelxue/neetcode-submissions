class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        queue = deque()# 存index
        result = []

        for i, num in enumerate(nums):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if queue[0] <= i - k:
                queue.popleft()
            if i >= k - 1:
                result.append(nums[queue[0]])
        return result