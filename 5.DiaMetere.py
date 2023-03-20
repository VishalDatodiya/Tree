def diameterOfBinaryTree(root):
    def solve(root,dia):
        if root == None:
            return 0,dia

        lh, dia = solve(root.left,dia)
        rh, dia = solve(root.right,dia)
        max_dia = lh + rh
        dia = max(dia, max_dia)
        return max(lh, rh) + 1, dia
    h, dia = solve(root, 0)
    return dia

