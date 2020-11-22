class Queue():
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def enqueue(self,data):
        #empty the stack 1 and store in stack 2
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        #store the data
        self.s1.append(data)

        #restack the elements in stack 1
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def dequeue(self):
        #if the stack is empty return None
        if len(self.s1) == 0 :
            print("Queue is empty")
        else :
            return self.s1.pop()

    def printfront(self):
        #if queue is empty
        if len(self.s1) == 0 :
            print("Queue is empty")
        else :
            print(self.s1[-1])



#driver code
flag = 1
print("Choose your query")
print("1. x: Enqueue element into the end of the queue")
print("2. Dequeue the element at the front of the queue.")
print("3. Print the element at the front of the queue.")
print("4. Exit")
q = Queue()
while(flag==1):
    x = int(input("Enter your choice"))
    if(x==1):
        data = eval(input("Enter the data value"))
        q.enqueue(data)
    elif (x==2):
        a = q.dequeue()
        if a != None :
            print(a," is dequeued")
    elif (x==3):
        q.printfront()
    elif (x==4):
        flag=0
        print("Program Ended")
