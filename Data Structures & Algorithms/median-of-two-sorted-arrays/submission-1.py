class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        left_length = (m + n + 1) // 2

        l, r = 0, m
        while l <= r:
            i = (l + r) // 2
            j = left_length - i

            max_left_1 = nums1[i - 1] if i > 0 else float('-inf')
            min_right_1 = nums1[i] if i < m else float('inf')
            max_left_2 = nums2[j - 1] if j > 0 else float('-inf')
            min_right_2 = nums2[j] if j < n else float('inf')

            if max_left_1 > min_right_2:
                r = i - 1
            elif max_left_2 > min_right_1:
                l = i + 1
            else:
                if (m + n) % 2:
                    return max(max_left_1, max_left_2)
                else:
                    return (max(max_left_1, max_left_2) + min(min_right_1, min_right_2)) / 2