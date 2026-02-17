class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_count = self.countNodes(root.left)
        right_count = self.countNodes(root.right)
        
        return 1 + left_count + right_count
