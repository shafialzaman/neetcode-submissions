# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:



        q1 = deque()
        q1.append([p,q])
        def dfs(a):
            while a:
                temp1,temp2 = a.popleft()
                if temp1 is None and temp2 is None:
                    continue
                if not temp1 or not temp2:
                    return False
                if temp1.val != temp2.val:
                    return False
                a.append([temp1.left,temp2.left])
                a.append([temp1.right,temp2.right])

            return True
        return dfs(q1)

        