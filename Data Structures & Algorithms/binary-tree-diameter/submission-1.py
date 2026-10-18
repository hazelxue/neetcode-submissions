# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        # returns height
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            # every node need to check their res, because max value not always at root
            self.res = max(self.res, left + right)
            # return height to next level to calculate max height
            return 1 + max(left, right)
        dfs(root)
        return self.res