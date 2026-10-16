class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #[left, right]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # mid in left interval
            elif nums[mid] >= nums[l]:
                # Monotonically increasing
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # mid in right interval
            else:
                # Monotonically increasing
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
