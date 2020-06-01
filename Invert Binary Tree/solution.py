# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        def reverse(root1,root2):
            if(root1.left):
                root2.right=TreeNode(root1.left.val)
                reverse(root1.left,root2.right)
                
            if(root1.right):
                root2.left=TreeNode(root1.right.val)
                reverse(root1.right,root2.left)
        
        if(root): 
            new_root = TreeNode(root.val)
            reverse(root,new_root)
            return new_root
