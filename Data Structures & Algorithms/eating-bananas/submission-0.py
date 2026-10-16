class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # try k = [1, 2,..., max(p)] in binary search
        # brute: O(max(p)*p)
        # binary search: O(log(max(p)*p))
        l, r = 1, max(piles)
        result = r
        while l <= r:
            k = (l + r) // 2
            hour = 0
            for p in piles:
                hour += math.ceil(p / k)

            if hour <= h:# = is vaild
                result = min(result, k)
                r = k - 1
            else:
                l = k + 1
        return result