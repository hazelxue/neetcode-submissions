class TimeMap:

    def __init__(self):
        self.store = {}#key: list of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])#not =

    def get(self, key: str, timestamp: int) -> str:
        res = ""#empty
        values = self.store.get(key, [])
        # binary search
        # values are already in sorted order accoarding to the question
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]# so far the best answer
                l = mid + 1
            else:
                # not a valid answer so do not update res
                r = mid - 1
        return res#either empty or a valid answer