class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
leaf5 = TreeNode(val=5)
leaf4 = TreeNode(val=4)
node2 = TreeNode(val=2,left=None,right=leaf4)
node3 = TreeNode(val=3,left=None,right=leaf5)
root = TreeNode(val=1,left=node2,right=node3)


def cousins(root,x,i,parent=None):
    j=-1
    if(root.val==x):
        return i,parent
    if(root.left):
        j,parent=cousins(root.left,x,i+1,root.val)
    if(j!=-1):
        return j,parent
    if(root.right):
        j,parent=cousins(root.right,x,i+1,root.val)
    if(j!=-1):
        return j,parent
    return -1,-1
    
    
x_i,x_parent=cousins(root,4,0)
y_i,y_parent=cousins(root,5,0)
print (x_i,x_parent)
print (y_i,y_parent)
if(x_i==y_i and x_parent!=y_parent):
    print ('cousins')
