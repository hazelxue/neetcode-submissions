class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sort by (value, index) 
        nums = sorted((n, i) for i, n in enumerate(nums))
        left, right = 0, len(nums) - 1
        while left < right:
            s = nums[left][0] + nums[right][0]
            if s > target:
                right -= 1
            elif s < target:
                left += 1
            else:
                if nums[left][1] < nums[right][1]:
                    return [nums[left][1], nums[right][1]]
                return [nums[right][1], nums[left][1]]
