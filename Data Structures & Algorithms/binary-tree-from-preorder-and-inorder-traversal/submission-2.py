# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}
        self.index_will_build = 0# in preorder:mid,l,r

        def build(l, r):
            if l > r:
                return None
            # middle
            root_val = preorder[self.index_will_build]
            mid = idx_map[root_val]
            self.index_will_build += 1
            root = TreeNode(root_val)
            # l, r
            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)
            return root
        return build(0, len(preorder) - 1)