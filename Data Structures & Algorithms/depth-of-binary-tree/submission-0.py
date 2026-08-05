# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root: return 0
        q = [[root,1]]

        while q:
            temp,val = q.pop()
            if temp:
                res = max(res,val)
                q.append([temp.left,val+1])
                q.append([temp.right,val+1])


        return res


        