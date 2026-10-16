class Solution:
    def findMin(self, nums: List[int]) -> int:
        #[left, right]
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:#vaild
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (l + r) // 2
            res = min(res, nums[mid])# 记录mid 因为后面就移动指针了
            if nums[mid] >= nums[l]:# = means min number on the right
                l = mid + 1
            else:
                r = mid - 1
        return res