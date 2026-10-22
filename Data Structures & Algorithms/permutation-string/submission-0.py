class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = [0] * 26
        for ch in s1:
            need[ord(ch) - ord("a")] += 1
        need_count = sum(1 for x in need if x > 0)
        
        window = [0] * 26
        left = 0
        valid = 0
        for right, c in enumerate(s2):
            idx = ord(c) - ord("a")
            window[idx] += 1
            if window[idx] == need[idx]:
                valid += 1
            
            if right - left + 1 > len(s1):
                left_idx = ord(s2[left]) - ord("a")
                if window[left_idx] == need[left_idx]:
                    valid -= 1
                window[left_idx] -= 1
                left += 1
            
            if right - left + 1 == len(s1) and valid == need_count:
                return True
        return False