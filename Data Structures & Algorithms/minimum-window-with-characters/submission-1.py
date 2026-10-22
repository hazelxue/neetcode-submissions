class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}
        left = 0
        valid = 0
        start = 0
        min_len = float('inf')
        for right, ch in enumerate(s):
            if ch in need:
                window[ch] = window.get(ch, 0) + 1
                if window[ch] == need[ch]:
                    valid += 1
            while valid == len(need):
                if right - left + 1 < min_len:
                    start = left
                    min_len = right - left + 1
                if s[left] in window:
                    if window[s[left]] == need[s[left]]:
                        valid -= 1
                    window[s[left]] -= 1
                left += 1
        if min_len == float('inf'):
            return ""
        return s[start: start + min_len]
