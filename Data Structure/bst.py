class Node:
    def __init__(self,key:int):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        
    def makeRoot(self, key:int) :
        self.root = Node(key)
        
    def traverse(self):
        return self.traverseNode(self.root)
    
    def traverseNode(self, currentNode:Node):
        rst = []
        if currentNode.left :
            rst+=self.traverseNode(currentNode.left)
        
        if currentNode : 
            rst+=currentNode.key
            
        if currentNode.right:
            rst+= self.traverseNode(currentNode.right)
            
        return rst

    #처음에 루트 넣어주기 위해 2개의 함수로 분리
    def search(self, targetKey:int):
        return self.searchKey(self.root, targetKey)
    
    def searchKey(self, currentNode:Node  , targetKey:int):
        if currentNode==None :
            return False
        
        if targetKey == currentNode.key :
            return currentNode
        
        if targetKey < currentNode.key :
            return self.search(currentNode.left, targetKey )
        
        if targetKey > currentNode.key : 
            return self.search(currentNode.right, targetKey)
    

    #처음에 루트 유무 확인위해 2개의 함수로 분리
    def insert(self, newKey:int):
        if self.root == None:
            self.makeRoot(newKey)
            return True
        
        else: 
            self.insertKey(self.root, newKey)

    
    def insertKey(self, currentNode:Node, newKey:int):
        if newKey <= currentNode.key:
            
            if currentNode.left : 
                self.insertKey(currentNode.left, newKey)
            
            else :
                currentNode.left = Node(newKey)
        else :
            if currentNode.right :
                self.insertKey(currentNode.right, newKey)
            
            else:
                currentNode.right = Node(newKey)
                
                
    # def delete(self, targetKey:int):
    #     return self.deleteKey(self.root, targetKey)
    
    # def deleteKey(self, currentNode:Node, targetKey:int):
