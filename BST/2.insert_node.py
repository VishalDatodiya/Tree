
class TreeNode:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None        

def insertIntoBST(root, val):
    if root == None:
        node = TreeNode(val)
        return node
    
    if root.val > val:
        root.left = insertIntoBST(root.left,val)
    else:
        root.right = insertIntoBST(root.right,val)
    return root