

# left - root - right

# Approach

# 1. add left side value in stack 
# 2. if we got None (root == None) then stop
# 3. pop the top value and print it
# 4. add the right side value   -> root = root.right

# hint -: use 2 loop inner loop for adding left side element



def inOrderIteratively(root):
    if root == None:
        return []
    
    stk = []
    ans = []
    
    while len(stk) > 0 or root != None:
        while root != None:
            stk.append(root)
            root = root.left
        
        root = stk.pop()
        ans.append(root.val)
        root = root.right
    return ans
