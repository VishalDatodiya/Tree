
# # 1. Basic Implementation of tree

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
        
# # PreOrder Traversal
# def printNode(root):
#     if root == None:
#         return
#     print(root.data, end=" ")
#     printNode(root.left)
#     printNode(root.right)


# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
     
# node1.left = node2
# node1.right = node3 
# node2.left = node4  

# printNode(node1)



# 2. Take input from user


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

# def printNode(root):
#     if root == None:
#         return
#     print(root.data, end=" ")
#     printNode(root.left)
#     printNode(root.right)

def printNode(root):
    if root == None:
        return
    print(root.data, end=":")
    if root.left != None:
        print(root.left.data, end=",")
    if root.right != None:
        print(root.right.data, end="")
    print()
    printNode(root.left)
    printNode(root.right)
     
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

# o/p

# 1:2,3
# 2:4,
# 4:
# 3: