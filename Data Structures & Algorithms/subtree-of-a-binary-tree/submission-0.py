# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # edge case
        if not subRoot: return True
        if not root: return False
        # make sure trees are not empty
        if self.sametree(root, subRoot):
            return True
        # recursive
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))

    def sametree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (self.sametree(s.left, t.left) and 
                    self.sametree(s.right, t.right))
        return False