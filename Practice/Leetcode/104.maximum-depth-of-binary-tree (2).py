#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        stack = []
        depth = 0
        if root:
            stack.append((1, root))
        while stack:
            cd, root = stack.pop()
            if root:
                depth = max(cd,depth)
                stack.append((cd+1,root.left))
                stack.append((cd+1,root.right))
        return depth

        
# @lc code=end

