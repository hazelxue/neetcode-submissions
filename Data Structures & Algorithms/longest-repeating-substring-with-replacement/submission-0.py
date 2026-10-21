class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        maxCount = 0#当前窗口最大字符频率
        maxLength = 0
        for right in range(len(s)):
            # 扩展右边界，更新计数
            count[s[right]] = count.get(s[right], 0) + 1
            maxCount = max(maxCount, count[s[right]])

            winLength = right - left + 1
            # 不合法，收缩左边界，不必更新maxcount（没用）
            if winLength - maxCount > k:
                count[s[left]] -= 1
                left += 1
            
            maxLength = max(maxLength, right - left + 1)
        return maxLength