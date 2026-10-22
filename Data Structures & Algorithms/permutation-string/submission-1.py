class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 防一手p大于s的情况
        if len(s1) > len(s2):
            return False
        # 需要什么
        need = [0] * 26
        for ch in s1:
            need[ord(ch) - ord("a")] += 1
        # 需要几个类型字母
        need_count = sum(1 for x in need if x > 0)
        # 有什么
        window = [0] * 26
        left = 0
        # 有几个合格数量的字母
        valid = 0
        for right, c in enumerate(s2):
            # 加入新的，更新window valid
            idx = ord(c) - ord("a")
            window[idx] += 1
            if window[idx] == need[idx]:
                valid += 1
            # 去掉旧的（维持窗口长度不变），更新window valid left
            if right - left + 1 > len(s1):
                left_idx = ord(s2[left]) - ord("a")
                if window[left_idx] == need[left_idx]:
                    valid -= 1
                window[left_idx] -= 1
                left += 1
            # 此时是不是长度一致，valid一致
            if right - left + 1 == len(s1) and valid == need_count:
                return True
        return False