# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # node, low, high → bool
        # root none
        # middle, left, right
        def dfs(node, low, high):
            # return true/flase
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return (dfs(node.left, low, node.val) and dfs(node.right, node.val, high))
        return dfs(root, float('-inf'), float('inf'))



