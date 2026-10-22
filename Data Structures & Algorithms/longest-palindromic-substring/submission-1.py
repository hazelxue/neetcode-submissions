class Solution:
    def longestPalindrome(self, s: str) -> str:

        start = 0
        max_len = 0
        def expand_from_center(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1
        
        for i in range(len(s)):
            # aba
            l, r = expand_from_center(s, i, i)
            if r - l + 1 > max_len:
                start = l
                max_len = r - l + 1
            # abba
            if i + 1 < len(s):
                l, r = expand_from_center(s, i, i + 1)
                if r - l + 1 > max_len:
                    start = l
                    max_len = r - l + 1
        return s[start: start + max_len]