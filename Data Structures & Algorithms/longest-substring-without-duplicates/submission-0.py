class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # the lastest index that the chr occur
        char_index = {}
        max_len = 0
        # window start
        left = 0

        # right: window end
        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
            max_len = max(max_len, right - left + 1)
        return max_len