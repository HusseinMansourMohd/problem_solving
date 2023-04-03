## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode] , min_val : float , max_val : float) -> bool:
            if not node:
                return True
            if not min_val < node.val < max_val:
                return False