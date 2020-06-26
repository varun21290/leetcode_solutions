class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if(not root):return 0
        
        stack_val=''
        s=0
        
        def dfs(node,stack_val,s):
            if(not node): 
                return stack_val,s
            
            stack_val=stack_val+str(node.val)
            
            if(not node.left and not node.right): 
                s+=int(stack_val)
                
            stack_val,s=dfs(node.left,stack_val,s)
            stack_val,s=dfs(node.right,stack_val,s)
            stack_val=stack_val[0:len(stack_val)-1]
            return stack_val,s
        
        
        _,s=dfs(root,stack_val,s)
        return s
