class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def bstFromPreorder(self, preorder: [int]) -> TreeNode:
        root=TreeNode(preorder[0])
        for i in range(1,len(preorder)):
            node=root
            while(node):
                if(node.val>preorder[i]):
                    if(node.left): node = node.left
                    else: 
                        node.left = TreeNode(preorder[i])
                        break
                if(node.val<preorder[i]):
                    if(node.right): node=node.right
                    else:
                        node.right = TreeNode(preorder[i])
                        break
        return root
