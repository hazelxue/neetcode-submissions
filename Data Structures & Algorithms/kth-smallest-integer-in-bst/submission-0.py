# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #pop in order, res=the kth pop item
        stack = []
        cur = root

        while cur or stack:
            # ① 一路往左，把路过的节点压进栈
            while cur:
                stack.append(cur)
                cur = cur.left

            # ② 弹出栈顶，访问它
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val

            # ③ 转到右子树
            cur = cur.right