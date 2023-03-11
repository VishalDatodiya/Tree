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


def NodesAtKDistance(root,k):
    if root == None:
        return
    if k == 0:
        print(root.data,end=" ")
        return
    NodesAtKDistance(root.left,k-1)
    NodesAtKDistance(root.right,k-1)
    
    
    # 11                0      
# 12      13        1       1

def ReplaceNodeWithDept(root, d=0): # d is a variable with default value 0
    if root == None:
        return
    root.data = d
    ReplaceNodeWithDept(root.left,d+1)
    ReplaceNodeWithDept(root.right,d+1)
     
# Find Node in tree
def isNodePresent(root, x):
    if root == None:
        return False
    if root.data == x:
        return True

    left = isNodePresent(root.left,x)
    right = isNodePresent(root.right,x)
    return left or right  

# Node without siblings

def printNodesWithoutSibling(root) :
    if root == None:
        return -1
    
    if printNodesWithoutSibling(root.left) == -1 and root.right != None:
        print(root.right.data, end=" ")
    if printNodesWithoutSibling(root.right) and root.left != None:
        print(root.left.data, end=" ")


def removeLeafNodes(root):
    if root == None:
        return None
    
    if root.left == None and root.right == None:
        return None
    
    root.left = removeLeafNodes(root.left)
    root.right = removeLeafNodes(root.right)
    
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

print("Total nodes : ",countNodes(root))
print("Total leaf nodes : ", CountLeaf(root))
print("total sum of nodes : ", sumOfNodes(root))
print("Max node : ", findMaxNode(root))
print("Min node : ", findMinNode(root))
print("Height of Tree : ", HeightOfTree(root))
print("Nodes At k distance : ")
NodesAtKDistance(root,k=2)
print("replace node with k dept : ")
ReplaceNodeWithDept(root)
printNode(root)
print("Node is Present : ",isNodePresent(root,5))
print("Nodes without siblings : ")
printNodesWithoutSibling(root)

removeLeafNodes(root)
printNode(root)