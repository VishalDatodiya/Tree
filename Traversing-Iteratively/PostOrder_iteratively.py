

# Left - right - root

# Approach

# Using 2 stack

# 1. add root in stk1
# 2. pop top element from stk1 and append in stk2(ans)
# 3. add first left and right node of popped node
# 4. reverse the stk2 (ans)

def postOrderIteratively(root):
    if root == None:
        return []
    stk = [root]
    ans = []

    while stk:
        node = stk.pop()
        ans.append(node.val)
        if node.left != None:
            stk.append(node.left)
        if node.right != None:
            stk.append(node.right)
    return ans[::-1]
