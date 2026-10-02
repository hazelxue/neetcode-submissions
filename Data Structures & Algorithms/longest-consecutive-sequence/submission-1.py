class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0

        for num in nums:
            if num - 1 in nums:
                continue
            else:
                cur = num
                len_ = 1
                while cur + 1 in nums:
                    len_ += 1
                    cur += 1
                max_len = max(len_, max_len)
        return max_len