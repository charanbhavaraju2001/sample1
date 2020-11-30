#Python Program to perform Binary Tree Traversals
#We have seen Levelorder,Inorder,Postorder,Preorder Traversals

#Binary Tree Node
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

#Levelorder traversal 
def printLevelorder(root):
    h = height(root)
    for i in range(1,h+1):
        printGivenlevel(root,i)

def printGivenlevel(root,level):
    if root == None:
        return
    if level == 1 :
        print(root.data,end = " ")
    elif level > 1 :
        printGivenlevel(root.left,level-1)
        printGivenlevel(root.right,level-1)

def height(node):
    if node == None :
        return 0
    else :
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight :
            return lheight+1
        else:
            return rheight+1

def printInorder(root):
    if root :
        printInorder(root.left)

        print(root.data,end = " ")

        printInorder(root.right)

def printPreorder(root):
    if root :
        print(root.data,end = " ")

        printPreorder(root.left)

        printPreorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)

        printPostorder(root.right)

        print(root.data,end = " ")




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("\nInorder Traversal of the Tree is :\n")
printInorder(root)
print("\nPreorder Traversal of the Tree is :\n")
printPreorder(root)
print("\nPostorder Traversal of the Tree is :\n")
printPostorder(root)
print("\nLevelorder Traversal of the Tree is :\n")
printLevelorder(root)
