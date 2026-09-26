# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max = float("-inf")
        self.dfs_post(root)
        return self.global_max

    def dfs_post(self, cursor):
        # traverse left side
        if cursor is None:
            return 0

        left_non_diverged_sum = self.dfs_post(cursor.left)
        # traverse right side
        right_non_diverged_sum = self.dfs_post(cursor.right)
        
        # do something on current cursor. i.e., the path must pass through this node.
        # this node does not use only one divergence chance
        non_diverged_sum = cursor.val + max(left_non_diverged_sum, right_non_diverged_sum, 0)
        diverged_sum = cursor.val + left_non_diverged_sum + right_non_diverged_sum
        max_path_sum_passing_cursor = max(non_diverged_sum, diverged_sum)
        if self.global_max < max_path_sum_passing_cursor:
            self.global_max = max_path_sum_passing_cursor
        return non_diverged_sum

        