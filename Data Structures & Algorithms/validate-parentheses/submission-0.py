class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        for c in s:
            if c == "(":
                queue.append(")")
            elif c == "{":
                queue.append("}")
            elif c == "[":
                queue.append("]")
            elif not queue or queue[-1] != c:
                return False
            else:
                queue.pop()
        return True if not queue else False
                