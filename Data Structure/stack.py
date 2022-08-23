#1. array
class arrayStack:
    def __init__(self):
        self.array  = [] #maxSize 설정. 
        self.maxSize = 1000
        self.top = -1

    def isEmpty(self):
        if self.top==-1:
            return True
        
        else:
            return False

    def isFull(self):
        return self.top==self.maxSize
    
    def push(self, data):
        if not self.isFull():
            self.array.append(data)
            self.top+=1
        
    def pop(self):
        if self.isEmpty():
            return -1
        data = self.array[self.top]
        self.top-=1
        return data
    def peek(self):
        if self.isEmpty():
            return -1
        data = self.array[self.top]
        return data

#2. linked list

class Node:
    def __init__(self, data=0, link=None):
        self.data = data
        self.link = link
class Stack:
    def __init__(self):
        self.top = None
  
    def isEmpty(self):
        if self.top != None:
             return False
        return True
    

    def push(self, data):
        newNode = Node(data)
        newNode.link = self.top
        self.top = newNode
        
    def pop(self):
        if not self.isEmpty():
            
            data = self.top.data
            self.top = self.top.link
            return data
    
    def peek(self):
        if not self.isEmpty():

            return self.top.data
        
# s = arrayStack()
# s.push(1)
# s.push(2)
# s.push(3)
# p1 = s.pop()
# print(p1)