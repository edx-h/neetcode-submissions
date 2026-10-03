# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # use dfs
        self.k = k
        _, max_val = self.dfs(root, 0)
        return max_val

    def dfs(self, cursor, counter):
        if cursor is None:
            return counter, None

        counter, max_val = self.dfs(cursor.left, counter)
        if counter == self.k:
            return counter, max_val
        # do something here
        max_val = cursor.val
        counter += 1
        if counter == self.k:
            return counter, max_val
        return self.dfs(cursor.right, counter)