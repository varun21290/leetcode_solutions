# Definition for a binary tree node.

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k=k
        def inorder(root):
            inorder_list=[]
            if(root.left and self.k>0):
                inorder_list.extend(inorder(root.left))
            if(self.k>0):
                inorder_list.append(root.val)
                self.k-=1
            if(root.right and self.k>0):
                inorder_list.extend(inorder(root.right))
            return inorder_list
        
        return inorder(root)[-1]
    
    def kthSmallest1(self, root: TreeNode, k: int) -> int:
        def inorder(root):
            inorder_list=[]
            if(root.left): 
                inorder_list.extend(inorder(root.left))
            inorder_list.append(root.val)
            if(root.right):
                inorder_list.extend(inorder(root.right))
            return inorder_list
        
        return inorder(root)[k-1]
