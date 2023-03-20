
# Only for unique element

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    
    def __init__(self) -> None:
        self.root = None
        
    def insert(self,node,val):
        if node.data >= val:
            if node.left == None:
                node.left = Node(val)
            else:
                self.insert(node.left, val)
            
        if node.data < val:
            if node.right == None:
                node.right = Node(val)
            else:
                self.insert(node, val)
        
    def insertNode(self,arr):
        for val in arr:
            if self.root == None:
                self.root = Node(val)
            else:
                self.insert(self.root,val)
    
    def traverse(self, node):
        if node == None:
            return 
        print(node.data, end=" ")
        self.traverse(node.left)
        self.traverse(node.right)
        return 
    
    def PrintNodes(self):
        self.traverse(self.root)

# only for unique element
arr = [5,3,1,6,4,2]          
bst = BST()
bst.insertNode(arr)
bst.PrintNodes()

