
import queue

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

def printNodesLevelWise(root):
    if root == None:
        return None
    q1 = queue.Queue()
    q1.put(root)
    while not q1.empty():
        cur_node = q1.get()
        print(cur_node.data, end=" ")
        if cur_node.left != None:
            q1.put(cur_node.left)
        if cur_node.right != None:
            q1.put(cur_node.right)


    
def takeInputLevelWise():
    print("Root data : ")
    root_data = int(input())
    if root_data == -1:
        return None
    q1 = q2 = queue.Queue()
    root = Node(root_data)
    q1.put(root)
    while not q1.empty():
        cur_node = q1.get()
        print("left chile of : ", cur_node.data)
        
        left = int(input())
        if left != -1:
            left_child = Node(left)
            cur_node.left = left_child
            q2.put(left_child)
    
        print("Right Child of : ",cur_node.data)
        right = int(input())
        if right != -1:
            right_child = Node(right)
            cur_node.right = right_child
            q2.put(right_child)
        q1,q2 = q2,q1

    return root

root = takeInputLevelWise()
printNodesLevelWise(root)
