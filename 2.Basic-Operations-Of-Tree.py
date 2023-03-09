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

def countNodes(root):
    if root == None:
        return 0
    left = countNodes(root.left)
    right = countNodes(root.right)
    return left + right + 1

def sumOfNodes(root):
    if root == None:
        return 0
    left = sumOfNodes(root.left)
    right = sumOfNodes(root.right)
    return left + right + root.data

def CountLeaf(root):
    if root == None:
        return 0
    left = CountLeaf(root.left)
    right = CountLeaf(root.right)
    if root.left == None and root.right == None:
        return left + right + 1
    return left + right

def findMinNode(root):
    if root == None:
        return 100000
    left = findMinNode(root.left)
    right = findMinNode(root.right)
    return min(left, right, root.data)

def findMaxNode(root):
    if root == None:
        return -1000000
    left = findMaxNode(root.left)
    right = findMaxNode(root.right)
    return max(left, right, root.data)

def HeightOfTree(root):
    if root == None:
        return 0
    left = HeightOfTree(root.left)
    right = HeightOfTree(root.right)
    if left >= right:
        return left + 1
    return right + 1

     
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

print("Total nodes : ",countNodes(root))
print("Total leaf nodes : ", CountLeaf(root))
print("total sum of nodes : ", sumOfNodes(root))
print("Max node : ", findMaxNode(root))
print("Min node : ", findMinNode(root))
print("Height of Tree : ", HeightOfTree(root))
