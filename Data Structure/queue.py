class arrayQueue:
    def __init__(self):
        self.array = []
        self.front = 0
        self.rear = 0
        self.maxSize = 1000
    def isEmpty(self):
        return self.front == self.rear #0 or 1
    
    def isFull(self):
        return self.rear == self.maxSize
    
    def push(self,data):
        if not self.isFull():
            self.array.append(data)
            self.rear+=1
        
    def pop(self):
        if not self.isEmpty():
            data = self.array[self.front]
            self.front+=1
            return data
        
    def peek(self):
        data = self.array[self.front]
        return data

class circleQueue:
    def __init__(self):
        maxSize = 10
        self.maxSize = maxSize+1 # front의 첫번째 공간부터 데이터를 넣지 않고 더미 공간 -> full / empty 구분
        self.front = 0
        self.rear = 0
        self.array = [None] * maxSize
        
    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear+1)%self.maxSize
    
    def push(self,data):
        if not self.isFull():
            self.rear = (self.rear+1)%self.maxSize
            self.array[self.rear] = data

    def pop(self):
        if not self.isEmpty():
            self.front = (self.front+1)%self.maxSize
            return self.array[self.front]
            
    def peek(self):
        if not self.isEmpty():
            return self.array[self.front+1]
        
class Node:
    def __init__(self,data=0, link=None):
        self.data = data
        self.link = link
    
class Queue:
    #front에서 pop, rear에서 in
    def __init__(self):
        self.front = 0
        self.rear = 0
    
    def isEmpty(self):
        if self.front == 0 and self.rear==0:
            return True
        else:
            return False
    
    def push(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.link = newNode
            self.rear = newNode
    
    def pop(self):
        if not self.isEmpty():
            data = self.front
            self.front = self.front.link
            return data.data
        
    def peek(self):
        if not self.isEmpty():
            return self.front.data

# q =arrayQueue()
# q.push(1)
# q.push(2)
# p1 = q.pop()
# print(p1)
# q.push(3)
# p3 = q.pop()
# print(p3)
        
        
            
