
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

def printNode(root):
    if root == None:
        return
    print(root.data, end=" ")
    printNode(root.left)
    printNode(root.right)


def mirrorBinaryTree(root) :
    if root == None:
        return None
    
    temp1 = mirrorBinaryTree(root.left)
    temp2 = mirrorBinaryTree(root.right)

    root.left = temp2
    root.right = temp1
    return root


def takeInput():
    print("Root Data: ")
    root_data = int(input())
    
    # if node don't have any child node
    if root_data == -1:
        return
    
    root = Node(root_data)
    print("left data of : ",root.data)
    root.left = takeInput()
    print("right data of : ",root.data)
    root.right = takeInput()
    
    return root

root = takeInput()
printNode(root)
print()
root = mirrorBinaryTree(root)
printNode(root)