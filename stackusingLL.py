class Node :
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack :
    def __init__(self):
        self.top = -1
        self.root = None

    def push(self,key):
        new_node = Node(key)
        if self.root==None:
            self.root = new_node
            self.top +=1
        else :
            temp = self.root
            while(temp.next):
                temp = temp.next
            temp.next = new_node
            self.top += 1

    def pop(self):
        if self.top == -1 and self.root == None:
            print("Stack Underflow")
            return None
        elif self.root.next == None :
            self.root = None
            return None
        else:
            temp = self.root
            while(temp.next.next):
                temp = temp.next
            temp.next = None
            self.top -= 1
            return self.root

    def peek(self):
        if self.top == -1 :
            print("Stack Underflow")
        else :
            temp = self.root
            while(temp.next):
                temp = temp.next
            print(temp.data)

head = Stack()
head.push(10)
head.peek()
head.push(20)
head.push(30)
head.peek()
head.pop()
head.peek()
