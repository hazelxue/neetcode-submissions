class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # trick
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        l = 0
        r = fast
        while l != r:
            l = nums[l]
            r = nums[r]
        return l