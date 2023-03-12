
# Not optimized O(N*N)

def isBalanced(root):

    def hbt(root):
        if root == None:
            return 0
        
        l = hbt(root.left)
        r = hbt(root.right)
        if l >= r:
            return l + 1
        return r + 1

    if root == None:
        return True

    h1 = hbt(root.left)
    h2 = hbt(root.right)

    if abs((h1+1)-(h2+1)) > 1:
        return False
    
    left = isBalanced(root.left)
    right = isBalanced(root.right)
    return left and right


# O(n)

def isBalanced(root):
    
    def solve(root):
        if root == None:
            return 0, True

        lh1,s1 = solve(root.left)
        rh1,s2 = solve(root.right)

        height = 1 + max(lh1, rh1)
        if abs(lh1-rh1) > 1:
            return height, False

        if s1 and s2:
            return height, True
        return height, False
    h, ans = solve(root)
    return ans