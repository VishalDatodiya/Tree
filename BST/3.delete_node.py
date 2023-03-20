

# Approach

# 1. find the node
# 2. we know that left side is always small and right is greater
# 3. so we disconnect roo and deleted node from it's right side
# 4. we connect deleted node -> right to the right (end node) of root's left  see line 32 or connect method


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def connect(self,root,temp):
    if root.right == None:
        root.right = temp
        return
    return self.connect(root.right,temp)

def deleteNode(root, key):
    if root == None:
        return None
    
    if root.val == key:
        if root.left != None:
            if root.right != None:
                temp = root.right
                root.right = None
                connect(root.left,temp)
                return root.left
            else:
                return root.left
        else:
            return root.right

    if root.val > key:
        root.left = deleteNode(root.left,key)
    else:
        root.right = deleteNode(root.right,key)
    return root