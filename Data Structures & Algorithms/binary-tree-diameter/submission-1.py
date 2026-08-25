# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # res = 0
        def dfs(root):

            if not root:
                return 0, 0
            leftheight, leftdiameter = dfs(root.left)
            rightheight, rightdiameter = dfs(root.right)

            height = 1 + max(leftheight,rightheight)

            diameter = max(leftheight+rightheight,leftdiameter,rightdiameter)
            return height, diameter
        
        height, diameter = dfs(root)
        return diameter