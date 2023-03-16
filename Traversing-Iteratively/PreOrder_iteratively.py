
# root - left - right

# Approach
# 1. add the root in stack
# 2. Add right child first then left
# 3. get top element from stack and print it



def preOrderIteratively(root):
    if root == None:
        return []
    stk = [root]
    ans = []
    while stk:
        node = stk.pop()
        ans.append(node.val)
        if node.right != None:
            stk.append(node.right)
        if node.left != None:
            stk.append(node.left)
    return ans