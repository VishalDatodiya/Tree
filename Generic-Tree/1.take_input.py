# there are 2 methods to take input

# 1. take the all child in list and then ask for 0th index child that how many child do you have and so on..


# 2. recursively

    # 1 take root data
    # 2 ask how many child root data have suppose n
    # 3 use loop till n
    # 4 call take input 
    # 5 append child in rood data list
    # 6 return root
    
    
class Node:
    def __init__(self, data):
        self.data = data
        self.children = list()
        

# 1. Print iteratively

import queue
def printTree(root):
    if root == None:
        return
    q1 = queue.Queue()
    q2 = queue.Queue()
    q1.put(root)
    while q1.qsize() > 0:
        while q1.qsize() > 0:
            root = q1.get()
            print(root.data, end=" : ")
            for i in root.children:
                print(i.data, end=",")    
                q2.put(i)
            print()
        q1,q2 = q2,q1


# 2. print recursively   

def printTreeRecursively(root):
    if root == None:
        return
    print(root.data, end=" : ")
    for child in root.children:
        print(child.data, end=",")
    print()
    for i in root.children:
        printTreeRecursively(i)
    
         

def takeInput():
    print("Enter root data :")
    root_data = int(input())
    if root_data == -1:
        return
    
    root = Node(root_data)
    
    # how many children
    print("how many children ",root_data)
    n = int(input())
    
    for i in range(n):
        child = takeInput()
        root.children.append(child)
    return root

root = takeInput()
# printTree(root)
printTreeRecursively(root)
